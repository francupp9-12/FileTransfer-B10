BUFFER_SIZE = 17000
MAX_FILE_SIZE = 1000000000  # 100 MB

START_MESSAGE = 0
DOWNLOAD = 0
UPLOAD = 1
MAX_FILE_REACHED = "File surpasses size limits"
ACK_SYN = 3
SEQN_LENGTH = 4
TIMEOUT_SECONDS = 3
HANDSHAKE_SIZE = 32
# Protocol
SELECTIVE_REPEAT = 1
STOP_AND_WAIT = 0

# Operation types
START = 0
DATA = 1
ERROR = 2
ACK = 3
INVALID_OP = 4
FIN = 5
ACK_FIN = 6
ACK_POS = 4
MAX_TIMEOUTS = 10
#STD_PACKET_SIZE = 16384
STD_PACKET_SIZE = 8000
MAX_SEQ_NUMBER = 99999
DATA_START = 5
MAX_CLIENTS_CONNECTED = 10
#ACK
ACK_SIZE = 5