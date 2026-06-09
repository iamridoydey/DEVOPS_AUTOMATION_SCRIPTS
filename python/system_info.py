import platform
import psutil


def byte_to_gb(byte):
  return byte / (1024**3)

def demarcate_line(subject):
  demarcate = "=" * 20
  print(demarcate, subject, demarcate)


# OS information
demarcate_line("OS info")
print(f"Operating system: {platform.system()} {platform.release()}")
print(f"Node name: {platform.node()}")
print(f"Architecture: {platform.machine()}")


# CPU information
demarcate_line("CPU info")
print(f"Physical cores: {psutil.cpu_count(logical=False)}")
print(f"Total threads: {psutil.cpu_count(logical=True)}")
print(f"Current usage: {psutil.cpu_percent(interval=1)}%")


# Memory information
demarcate_line("Memory info")
virtual_memory=psutil.virtual_memory()
memory_in_gb=byte_to_gb(virtual_memory.total)
swap_memory=psutil.swap_memory().total

print(f"Total memory: {memory_in_gb:.2f}GB")

if swap_memory > 0:
  print(f"Swap memory: {byte_to_gb(swap_memory):.2f}GB")
else:
  print(f"Swap memory yet to configured")

print(f"Memory usage: {virtual_memory.percent}%")


# Disk information
demarcate_line("Disk info")
disk=psutil.disk_usage('/')
disk_total=byte_to_gb(disk.total)
print(f"Total disk : {disk_total:.2f}GB")
print(f"Disk usage: {disk.percent}%")