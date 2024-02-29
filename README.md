# todoist-export-completed
Export all your completed Todoist tasks into a JSON file. Using Todoist's v9 API.
The program will run until the API does not return any new completed tasks.
Meant to run on MacOS or Linux.

**Note: The amount of tasks you can export may be limited by your Todoist plan.**

## Examples

Running the script

![running-todoist-export-completed](https://github.com/6C656F/todoist-export-completed/assets/97500607/3ec1ac46-0cb0-406f-b966-4b070702fb50)

Output (after `jq`)
![output](https://github.com/6C656F/todoist-export-completed/assets/97500607/09beb80e-e531-4432-84e6-f4d39c1c8232)


## Dependencies
### Python
`requests`

On MacOS/Ubuntu - `pip3 install requests`

## To Run
1. Find your Todoist API key [![Guide](https://todoist.com/help/articles/find-your-api-token-Jpzx9IIlB)](https://todoist.com/help/articles/find-your-api-token-Jpzx9IIlB)
2. Enter your API key in the variable `api_token`. 
3. `python3 todoist-export-completed.py` 

## Output
The script will run and output the entire response in `todoist_tasks_incremental.json`, in the same directory as the script.

The default output isn't organized. To fix this, simply run `jq '.[]' todoist_tasks_incremental.json > output.json`. 

This will format the JSON into `output.json` and make it readable. You can download `jq` from `brew` or `apt`, depending on what OS you are running. 

### Too many tasks?

If you have too many tasks, change `max_tasks` on line 4 to be a higher number. This increases the amount of pages to request. The program will automatically exit once the API stops returning tasks. 
