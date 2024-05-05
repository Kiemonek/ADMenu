"""Description: Constants for the frame and widgets in the application."""

#Window configuration
WINDOW_WIDTH = 860
WINDOW_HEIGHT = 480
WINDOW_TITLE = "AD Menu"
WIDTH_RESIZABLE = False
HEIGHT_RESIZABLE = False
WINDOW_BG_CLR = "#1E1E1E"
BAR_BG_CLR = "#838383"

#Database constants
DBFILENAME = "AD Menu\\data\\btn_database.json"
RSATFILENAME = "AD Menu\\data\\rsat_status.txt"
RSATSTATUSFILENAME = "AD Menu\\data\\status.txt"
FILEPATH = "AD Menu\\data"

#Buttons constants
BTN_FONT_DETAILS = ("Microsoft YaHei", 12, "bold")
BTN_FG_CLR = '#838383'
BTN_BG_CLR = '#1E1E1E'
BTN_ACTIVE_BG_CLR = '#838383'
#Button status texts
BTN_ADD_NEW = "Add New Button"
BTN_SAVE = "Save"
BTN_OK = "OK"
#Bottom banner button texts
BTN_CONNECT = "Connect"
BTN_ADD = "Add"
BTN_MODIFY = "Modify"
BTN_REMOVE = "Remove"

#Label constants
LBL_FONT_DETAILS = ("Microsoft YaHei", 19, "bold")
#Label colors
LBL_FG_CLR = '#1E1E1E'
LBL_BG_CLR = '#838383'
LBL_CONNECT_FG_CLR = '#20830E'
LBL_ADD_FG_CLR = '#DBDB0A'
LBL_MOD_FG_CLR = '#D98307'
LBL_REM_FG_CLR = '#DF1A1A'
LBL_TOP_FG_CLR = '#838383'
LBL_TOP_BG_CLR = '#1E1E1E'
UNDERLINE_CLR = '#1E1E1E'
#Label texts for banner
TOP_CMD = "Press button to connect"
TOP_MOD = "Press button to modify"
TOP_RM = "Press button to remove"
TOP_ADD_BTN = "Add New Button"
TOP_MOD_BTN = "Modify Button"
TOP_SUCCESS = "Success!"
TOP_LIMIT = "Limit reached!"
#Process status messages
STATUS_ADD = "Button added successfully!"
STATUS_MOD = "Button modified successfully!"
STATUS_RM = "Button removed successfully!"
STATUS_NO_BTN = "No buttons added yet"
STATUS_LIMIT = "List reached a limit of 48 buttons, remove or modify existing one."
#Label texts for button details
INSERT_TITLE = "Insert Button Name:"
INSERT_DOMAIN = "Insert Domain Name:"
INSERT_USERNAME = "Insert Username:"
INSERT_CONTROLLER = "Insert Domain Controller:"

#Options
OPTION_ADD = "add"
OPTION_RM = "rm"
OPTION_MOD = "mod"
OPTION_CMD = "cmd"
OPTION_LIMIT = "limit"
OPTION_TOP = "top"

#RSAT Status
RSAT_STATUS = "RSAT Status: "
RSAT_INSTALLED = "Installed"
RSAT_NOT_INSTALLED = "Not Installed"
RSAT_UNKNOWN = "Unknown"
RSAT_INSTALLATION = "Installing, click to update"
#RSAT Messagesboxes
RSAT_INFO_TITLE = "RSAT Modules"
RSAT_INFO_MESSAGE = "RSAT modules installed: "
RSAT_ASK_TITLE = "Install RSAT"
RSAT_ASK_MESSAGE = "Do you want to install RSAT modules?"
#Buffer
BUFFER_START = 0
BUFFER_FINISH = 10
BUFFER_SLEEP = 0.5
BUFFER_MESSAGE = "An error occurred while updating the status."
BUFFER_TITLE = "Error"
#PowerShell commands
CMD_COMMAND = 'powershell -Command'
PS_COMMAND = 'Get-WindowsCapability -Name RSAT* -Online | '
FORMAT_COMMAND = 'Format-List -Property State | '
INSTALL_COMMAND = 'Add-WindowsCapability -Online'
OUTPUT_COMMAND = 'Out-File -FilePath'
ENCODING_COMMAND = '-Encoding utf8'

#Assets
ASSET_PATH = "assets"
ASSET_ICON = "..\\assets\\icon.ico"

#Details exmaples
EXMPL_TITLE = "Company A"
EXMPL_DOMAIN = "companya.com"
EXMPL_USERNAME = "user1"
EXMPL_DOMAIN_CONTROLLER = "192.168.21.37"
