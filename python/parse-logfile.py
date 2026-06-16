from pathlib import Path

def extract_lines(logfile: str, keyword: str) -> list[str]:
  """
  Extract the lines which have the keyword
  Args:
    logfile: Path to the log file.
    keyword: Word which is matching in the log.
  Returns:
    List of matching lines.
  Raises:
    Raises FileNotFoundError if the logfile doesn't exist.
  """

  # Check whether the file exist or not
  p = Path(logfile)

  if not p.exists() or not p.is_file():
    raise FileNotFoundError(f"{logfile} doesn't exist")

  filter_logs = []
  with open(p, "r") as file:
    for line in file: 
      if keyword in line:
        filter_logs.append(line.strip())
  
  return filter_logs



def print_lines(filter_logs: list[str], keyword: str, logfile: str) -> None:
  """Print matched lines"""

  print(f"Searching {keyword} in file-> {logfile}.....")
  print("-" * 100)

  if not filter_logs:
    print(f"No lines containing '{keyword}' in {logfile}")
    return
  
  for log in filter_logs:
    print(log)

  print("-" * 100)

  print(f"Total {len(filter_logs)} matches found in the {logfile}")
  

if __name__ == "__main__":
  LOGFILE="./app.log"
  KEYWORD="ERROR"

  try:
    filter_logs = extract_lines(LOGFILE, KEYWORD)
    print_lines(filter_logs, KEYWORD, LOGFILE)
  except FileNotFoundError as e:
    print(f"Erro: {e}")
    sys.exit(1)