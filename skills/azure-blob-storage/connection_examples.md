# Azure Blob Storage Connection Examples

## Complete Working Examples

### Example 1: List All Containers and Blobs

```python
import os
from azure.storage.blob import BlobServiceClient

def list_all_data():
    """List all containers and their blobs."""
    # Get credentials from environment
    account_name = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
    account_key = os.getenv("AZURE_STORAGE_ACCOUNT_KEY")

    if not account_name or not account_key:
        raise ValueError("Azure Storage credentials not configured")

    # Create service client
    account_url = f"https://{account_name}.blob.core.windows.net"
    blob_service_client = BlobServiceClient(account_url, credential=account_key)

    # List containers
    print(f"Storage Account: {account_name}")
    print("\nContainers:")

    containers = blob_service_client.list_containers()
    for container in containers:
        print(f"\n  Container: {container.name}")

        # List blobs in each container
        container_client = blob_service_client.get_container_client(container.name)
        blobs = container_client.list_blobs()

        blob_count = 0
        total_size = 0
        for blob in blobs:
            blob_count += 1
            total_size += blob.size
            if blob_count <= 5:  # Show first 5 blobs
                size_mb = blob.size / (1024 * 1024)
                print(f"    - {blob.name} ({size_mb:.2f} MB)")

        if blob_count > 5:
            print(f"    ... and {blob_count - 5} more blobs")

        total_size_mb = total_size / (1024 * 1024)
        print(f"    Total: {blob_count} blobs, {total_size_mb:.2f} MB")

if __name__ == "__main__":
    list_all_data()
```

### Example 2: Download and Read Parquet File

```python
import os
import pandas as pd
from io import BytesIO
from azure.storage.blob import BlobServiceClient

def read_parquet_from_blob(container_name: str, blob_path: str) -> pd.DataFrame:
    """
    Download and read a Parquet file from Azure Blob Storage.

    Args:
        container_name: Name of the blob container
        blob_path: Path to the blob (e.g., "data/2024/sales.parquet")

    Returns:
        pandas DataFrame with the data
    """
    # Get credentials
    account_name = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
    account_key = os.getenv("AZURE_STORAGE_ACCOUNT_KEY")

    # Create blob client
    account_url = f"https://{account_name}.blob.core.windows.net"
    blob_service_client = BlobServiceClient(account_url, credential=account_key)

    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=blob_path
    )

    # Download blob content
    print(f"Downloading {blob_path} from container '{container_name}'...")
    download_stream = blob_client.download_blob()
    content = download_stream.readall()

    # Read as Parquet
    df = pd.read_parquet(BytesIO(content))
    print(f"Loaded DataFrame: {len(df)} rows, {len(df.columns)} columns")
    print(f"Columns: {list(df.columns)}")

    return df

# Usage example
if __name__ == "__main__":
    df = read_parquet_from_blob("sales-data", "2024/customer_sales.parquet")
    print(df.head())
```

### Example 3: Find All CSV Files in a Directory

```python
import os
from azure.storage.blob import BlobServiceClient
from typing import List, Dict

def find_csv_files(container_name: str, prefix: str = "") -> List[Dict]:
    """
    Find all CSV files in a container/directory.

    Args:
        container_name: Name of the blob container
        prefix: Optional directory prefix (e.g., "data/2024/")

    Returns:
        List of dicts with blob info (name, size, last_modified)
    """
    # Get credentials
    account_name = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
    account_key = os.getenv("AZURE_STORAGE_ACCOUNT_KEY")

    # Create client
    account_url = f"https://{account_name}.blob.core.windows.net"
    blob_service_client = BlobServiceClient(account_url, credential=account_key)

    container_client = blob_service_client.get_container_client(container_name)

    # List blobs with prefix
    blobs = container_client.list_blobs(name_starts_with=prefix)

    # Filter for CSV files
    csv_files = []
    for blob in blobs:
        if blob.name.endswith('.csv'):
            csv_files.append({
                'name': blob.name,
                'size': blob.size,
                'size_mb': blob.size / (1024 * 1024),
                'last_modified': blob.last_modified,
                'content_type': blob.content_settings.content_type if blob.content_settings else None
            })

    return csv_files

# Usage example
if __name__ == "__main__":
    files = find_csv_files("sales-data", prefix="2024/")
    print(f"Found {len(files)} CSV files:")
    for file in files:
        print(f"  - {file['name']} ({file['size_mb']:.2f} MB, modified: {file['last_modified']})")
```

### Example 4: Upload DataFrame as Parquet

```python
import os
import pandas as pd
from io import BytesIO
from azure.storage.blob import BlobServiceClient

def upload_dataframe_as_parquet(
    df: pd.DataFrame,
    container_name: str,
    blob_path: str,
    overwrite: bool = True
) -> str:
    """
    Upload a pandas DataFrame as a Parquet file to Azure Blob Storage.

    Args:
        df: DataFrame to upload
        container_name: Target container name
        blob_path: Target blob path (e.g., "output/results.parquet")
        overwrite: Whether to overwrite if blob exists

    Returns:
        URL of the uploaded blob
    """
    # Get credentials
    account_name = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
    account_key = os.getenv("AZURE_STORAGE_ACCOUNT_KEY")

    # Create client
    account_url = f"https://{account_name}.blob.core.windows.net"
    blob_service_client = BlobServiceClient(account_url, credential=account_key)

    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=blob_path
    )

    # Convert DataFrame to Parquet bytes
    buffer = BytesIO()
    df.to_parquet(buffer, index=False)
    buffer.seek(0)

    # Upload
    print(f"Uploading DataFrame to {blob_path}...")
    blob_client.upload_blob(
        buffer,
        overwrite=overwrite,
        content_settings={'content_type': 'application/octet-stream'}
    )

    blob_url = blob_client.url
    print(f"Upload complete: {blob_url}")

    return blob_url

# Usage example
if __name__ == "__main__":
    # Create sample DataFrame
    df = pd.DataFrame({
        'customer_id': [1, 2, 3],
        'revenue': [1000.50, 2500.75, 1750.25]
    })

    url = upload_dataframe_as_parquet(
        df,
        container_name="output-data",
        blob_path="processed/customer_revenue.parquet"
    )
```

### Example 5: Batch Download Multiple Files

```python
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from azure.storage.blob import BlobServiceClient
from typing import List

def download_blobs_parallel(
    container_name: str,
    blob_names: List[str],
    local_dir: str,
    max_workers: int = 5
) -> List[str]:
    """
    Download multiple blobs in parallel.

    Args:
        container_name: Container name
        blob_names: List of blob paths to download
        local_dir: Local directory to save files
        max_workers: Maximum concurrent downloads

    Returns:
        List of local file paths
    """
    # Get credentials
    account_name = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
    account_key = os.getenv("AZURE_STORAGE_ACCOUNT_KEY")

    # Create client
    account_url = f"https://{account_name}.blob.core.windows.net"
    blob_service_client = BlobServiceClient(account_url, credential=account_key)

    # Ensure local directory exists
    os.makedirs(local_dir, exist_ok=True)

    def download_blob(blob_name: str) -> str:
        """Download single blob."""
        blob_client = blob_service_client.get_blob_client(
            container=container_name,
            blob=blob_name
        )

        # Create local file path
        local_filename = os.path.basename(blob_name)
        local_path = os.path.join(local_dir, local_filename)

        # Download
        with open(local_path, "wb") as file:
            download_stream = blob_client.download_blob()
            file.write(download_stream.readall())

        return local_path

    # Download in parallel
    local_paths = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(download_blob, name): name for name in blob_names}

        for future in as_completed(futures):
            blob_name = futures[future]
            try:
                local_path = future.result()
                local_paths.append(local_path)
                print(f"Downloaded: {blob_name} -> {local_path}")
            except Exception as e:
                print(f"Error downloading {blob_name}: {e}")

    return local_paths

# Usage example
if __name__ == "__main__":
    blobs_to_download = [
        "2024/sales_jan.csv",
        "2024/sales_feb.csv",
        "2024/sales_mar.csv",
    ]

    local_files = download_blobs_parallel(
        container_name="sales-data",
        blob_names=blobs_to_download,
        local_dir="./downloads"
    )

    print(f"\nDownloaded {len(local_files)} files")
```

## Troubleshooting Tips

### Test Connection
```python
try:
    blob_service_client = BlobServiceClient(account_url, credential=account_key)
    # Try listing containers to test connection
    containers = list(blob_service_client.list_containers(max_results=1))
    print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")
```

### Check Blob Existence
```python
blob_client = blob_service_client.get_blob_client(container="my-container", blob="data/file.csv")
if blob_client.exists():
    props = blob_client.get_blob_properties()
    print(f"Blob exists: {props.size} bytes")
else:
    print("Blob does not exist")
```
