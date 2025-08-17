### Authentication

#### Configuring API keys

Get your API keys from <a href="https://www.5paisa.com/developerapi/apikeys" target="_blank">here</a>

Configure these keys in a file named `keys.conf` in the same directory as your python script exists

A sample `keys.conf` is given below:

```conf
[KEYS]
APP_NAME="5P57266562"
APP_SOURCE=18590
USER_ID="qkCEvW5TZzK"
PASSWORD="qtsazF5nfK0"
USER_KEY="Lk8A08LJ8qZ18U2IZnqgAdcKKF5OQipk"
ENCRYPTION_KEY="PlhL5fCmet0rXy75ZWTWnc20NJ21naTJ"
```

#### Login

```py
from py5paisa import FivePaisaClient

client = FivePaisaClient(email="venooogoapalacharie@gmail.com", passwd="Venu@115515", dob="19960101")
client.login()
```

After successful authentication, you should get a `Logged in!!` message.