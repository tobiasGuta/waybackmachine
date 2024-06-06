import requests

def get_all_wayback_snapshots(url):
    snapshots = []
    api_url = f"http://web.archive.org/cdx/search/cdx?url={url}&output=json"
    response = requests.get(api_url)
    data = response.json()
    if data and len(data) > 1:
        for snapshot_data in data[1:]:
            timestamp = snapshot_data[1]
            date = f"{timestamp[:4]}/{timestamp[4:6]}/{timestamp[6:8]}"  # Format as YYYY/MM/DD
            snapshot_url = f"http://web.archive.org/web/{timestamp}/{url}"
            snapshots.append((date, snapshot_url))
    return snapshots

def main():
    url = input("Enter the URL to check on Wayback Machine: ")
    snapshots = get_all_wayback_snapshots(url)
    if snapshots:
        print("Archived versions found:")
        for date, snapshot in snapshots:
            print(f"Date: {date}, URL: {snapshot}")
    else:
        print("No archived versions found for this URL.")

if __name__ == "__main__":
    main()
