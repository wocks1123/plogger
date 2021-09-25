# plogger


```python
from datetime import datetime

NOW = datetime.now().strftime('%Y%m%d%H%M%S')

logger = Logger(f"{NOW}.log")

logger.add("timestamp", timestamp)
logger.add("is_end", is_end)
logger.add("call_queue", )
logger.add("calls", calls)
logger.add("elevators")

logger.append_line()
```


```python
logger = Logger(logfile, write_mode=False)
ret = self.logger.get_object_from(0)
```