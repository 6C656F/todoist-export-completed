import requests
import json

def fetch_and_save_tasks_incrementally(api_token, filename='todoist_tasks_incremental.json', start_offset=0, limit=200, max_tasks=20000):
    base_url = "https://api.todoist.com/sync/v9/completed/get_all"
    offset = start_offset
    total_tasks_fetched = 0
    is_first_write = True

    with open(filename, 'w') as file:
        file.write('[')

    while offset < max_tasks:
        current_page = offset // limit + 1
        print(f"Fetching page {current_page} (offset {offset})...")

        response = requests.get(
            f"{base_url}?limit={limit}&offset={offset}",
            headers={"Authorization": f"Bearer {api_token}"}
        )
        if response.status_code == 200:
            data = response.json()
            tasks = data.get('items', [])
            if tasks:  # Check if there are tasks to ensure we don't append unnecessary commas
                total_tasks_fetched += len(tasks)
                print(f"Fetched {len(tasks)} tasks. Total fetched: {total_tasks_fetched}")

                # Append tasks to file
                with open(filename, 'a') as file:
                    # Prepend a comma only if this is not the first batch of tasks
                    if not is_first_write:
                        file.write(',')
                    else:
                        is_first_write = False  # Update the flag after the first write operation
                    json_str = ",".join(json.dumps(task) for task in tasks)
                    file.write(json_str)
            else:
                break  # No more tasks
        else:
            print(f"Failed to fetch tasks at offset {offset}. Status Code: {response.status_code}")
            break

        offset += limit

    # Close the JSON array in the file
    with open(filename, 'a') as file:
        file.write(']')

    print(f"All tasks have been saved to {filename}")

# Replace '<YOUR_API_TOKEN>' with your actual Todoist API token
api_token = '<YOUR_API_TOKEN'
fetch_and_save_tasks_incrementally(api_token)
