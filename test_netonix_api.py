import unittest
from netonix_api import Netonix

def get_test_config():
    return {
  "Config_Version": 90,
  "IPv4_Mode": "Static",
  "IPv4_Address": "1.2.3.4",
  "IPv4_Netmask": "255.255.0.0",
  "IPv4_Gateway": "1.2.0.1",
  "IPv4_Primary_DNS": "7.7.7.7",
  "IPv4_Secondary_DNS": "8.8.8.8",
  "IPv6_Enable": False,
  "IPv6_Mode": "DHCP",
  "IPv6_Address": "",
  "IPv6_Gateway": "",
  "IPv6_Primary_DNS": "",
  "IPv6_Secondary_DNS": "",
  "Switch_Name": "Switch1",
  "NTP_Zone": "America/New York (EST5EDT,M3.2.0,M11.1.0)",
  "Switch_Location": "",
  "GPS_Latitude": "",
  "GPS_Longitude": "",
  "Credentials_Name": "admin",
  "Credentials_Password": "",
  "Credentials_HashedPassword": "rtukisawegrsrs",
  "Credentials_NewHashedPassword": "$P$jflksajflkdsjlkfjdsalkfj/",
  "Credentials_Console_Login": False,
  "RADIUS_Enable": False,
  "RADIUS_Host": "",
  "RADIUS_Port": "1812",
  "RADIUS_Secret": "",
  "SSH_Enable": True,
  "SSH_Port": "22",
  "SSH_Allow_Passwords": True,
  "SSH_Allow_Telnet": True,
  "SSH_Keys": [],
  "SNMP_Server_Enable": True,
  "SNMP_Server_Community": "RO",
  "SNMP_Server_Contact": "",
  "SNMP_Server_Location": "",
  "Syslog_Enable": True,
  "Syslog_Host": "6.6.6.6",
  "Syslog_Port": "514",
  "Syslog_Exclude": "",
  "Syslog_Buffer_Size": "128",
  "SMTP_Enable": False,
  "SMTP_Host": "",
  "SMTP_Port": "25",
  "SMTP_Username": "",
  "SMTP_Password": "",
  "SMTP_Secure": False,
  "SMTP_Address": "",
  "SMTP_From_Address": "",
  "SMTP_Local_Hostname": "",
  "NTP_Enable": True,
  "NTP_Host": "pool.ntp.org",
  "STP_Enable": True,
  "STP_Version": "RSTP",
  "STP_Max_Age": "20",
  "STP_Hello_Time": "2",
  "STP_Forward_Delay": "15",
  "STP_Priority": "49152",
  "STP_LAG_Enable": True,
  "Storm_Control_Broadcast": "None",
  "Storm_Control_Multicast": "None",
  "Storm_Control_Unicast": "None",
  "Storm_Control_Loop_Protection": False,
  "Storm_Control_Pause_Frame": True,
  "PingWatchdogs": [],
  "PortBounces": [],
  "AccessControls": [],
  "HTTPS_Enable": True,
  "HTTPS_Port": "443",
  "HTTPS_Allow_HTTP": False,
  "HTTPS_HTTP_Port": "80",
  "AggregationMode_DestinationMAC": False,
  "AggregationMode_SourceMAC": False,
  "AggregationMode_SourceDestinationIP": True,
  "AggregationMode_SourceDestinationPort": False,
  "Tarpit_Enable": True,
  "Tarpit_Attempts": "5",
  "Tarpit_Delay": "60",
  "Discovery_Ubiquiti": True,
  "Discovery_Cisco": True,
  "Discovery_LLDP": True,
  "Auto_Backup_TFTP_URL": "",
  "Power_Hibernate_Voltage": "9",
  "Power_Wakeup_Voltage": "10",
  "Power_Warning_Voltage": "11",
  "Options_IGMP_Snooping": False,
  "QoSRules": [],
  "Options_Language": "en",
  "Serial_Mode": "Console",
  "Serial_TCP_Port": "502",
  "Serial_Baud_Rate": "115200",
  "Serial_Parity": "N",
  "Serial_Data_Bits": "8",
  "Serial_Stop_Bits": "1",
  "Email_Alerts_Link_Change": True,
  "Email_Alerts_Flow_Control": True,
  "Email_Alerts_DC_Power": True,
  "Email_Alerts_Fans": True,
  "Email_Alerts_PoE": True,
  "Email_Alerts_LACP": True,
  "Discovery_Discovery_Tab": True,
  "Switch_Revert_Timer": "180",
  "Applied": True,
  "Ports": [
    {
      "Number": 1,
      "Name": "",
      "Enable": True,
      "Link": "Auto",
      "PoE": "Off",
      "FlowControl": "Both",
      "Multicast": True,
      "MTU": "1528",
      "TxLimit": "",
      "RxLimit": "",
      "STP": True,
      "STPPriority": "128",
      "STP_Path_Cost": "",
      "Stats": True,
      "Isolation": False,
      "AllowedVLANs": "",
      "DHCP_Snooping": False,
      "Shutdown_Voltage": "",
      "Restart_Voltage": "",
      "Priority": "1",
      "Shutdown_Time": "",
      "Startup_Time": "",
      "Updated_SFP2": True,
      "QoSSched": "Strict",
      "PoE_Smart": True,
      "Updated_MTU": True,
      "Boot_Start_Delay": ""
    },
    {
      "Number": 2,
      "Name": "",
      "Enable": True,
      "Link": "Auto",
      "PoE": "Off",
      "FlowControl": "Both",
      "Multicast": True,
      "MTU": "1528",
      "TxLimit": "",
      "RxLimit": "",
      "STP": True,
      "STPPriority": "128",
      "STP_Path_Cost": "",
      "Stats": True,
      "Isolation": False,
      "AllowedVLANs": "",
      "DHCP_Snooping": False,
      "Shutdown_Voltage": "",
      "Restart_Voltage": "",
      "Priority": "2",
      "Shutdown_Time": "",
      "Startup_Time": "",
      "Updated_SFP2": True,
      "QoSSched": "Strict",
      "PoE_Smart": True,
      "Updated_MTU": True,
      "Boot_Start_Delay": ""
    },
    {
      "Number": 3,
      "Name": "",
      "Enable": True,
      "Link": "Auto",
      "PoE": "48V",
      "FlowControl": "Both",
      "Multicast": True,
      "MTU": "1528",
      "TxLimit": "",
      "RxLimit": "",
      "STP": True,
      "STPPriority": "128",
      "STP_Path_Cost": "",
      "Stats": True,
      "Isolation": False,
      "AllowedVLANs": "",
      "DHCP_Snooping": False,
      "Shutdown_Voltage": "",
      "Restart_Voltage": "",
      "Priority": "3",
      "Shutdown_Time": "",
      "Startup_Time": "",
      "Updated_SFP2": True,
      "QoSSched": "Strict",
      "PoE_Smart": True,
      "Updated_MTU": True,
      "Boot_Start_Delay": ""
    },
    {
      "Number": 4,
      "Name": "",
      "Enable": True,
      "Link": "Auto",
      "PoE": "48V",
      "FlowControl": "Both",
      "Multicast": True,
      "MTU": "1528",
      "TxLimit": "",
      "RxLimit": "",
      "STP": True,
      "STPPriority": "128",
      "STP_Path_Cost": "",
      "Stats": True,
      "Isolation": False,
      "AllowedVLANs": "",
      "DHCP_Snooping": False,
      "Shutdown_Voltage": "",
      "Restart_Voltage": "",
      "Priority": "4",
      "Shutdown_Time": "",
      "Startup_Time": "",
      "Updated_SFP2": True,
      "QoSSched": "Strict",
      "PoE_Smart": True,
      "Updated_MTU": True,
      "Boot_Start_Delay": ""
    },
    {
      "Number": 5,
      "Name": "",
      "Enable": True,
      "Link": "Auto",
      "PoE": "48V",
      "FlowControl": "Both",
      "Multicast": True,
      "MTU": "1528",
      "TxLimit": "",
      "RxLimit": "",
      "STP": True,
      "STPPriority": "128",
      "STP_Path_Cost": "",
      "Stats": True,
      "Isolation": False,
      "AllowedVLANs": "",
      "DHCP_Snooping": False,
      "Shutdown_Voltage": "",
      "Restart_Voltage": "",
      "Priority": "5",
      "Shutdown_Time": "",
      "Startup_Time": "",
      "Updated_SFP2": True,
      "QoSSched": "Strict",
      "PoE_Smart": True,
      "Updated_MTU": True,
      "Boot_Start_Delay": ""
    },
    {
      "Number": 6,
      "Name": "",
      "Enable": True,
      "Link": "Auto",
      "PoE": "48V",
      "FlowControl": "Both",
      "Multicast": True,
      "MTU": "1528",
      "TxLimit": "",
      "RxLimit": "",
      "STP": True,
      "STPPriority": "128",
      "STP_Path_Cost": "",
      "Stats": True,
      "Isolation": False,
      "AllowedVLANs": "",
      "DHCP_Snooping": False,
      "Shutdown_Voltage": "",
      "Restart_Voltage": "",
      "Priority": "6",
      "Shutdown_Time": "",
      "Startup_Time": "",
      "Updated_SFP2": True,
      "QoSSched": "Strict",
      "PoE_Smart": True,
      "Updated_MTU": True,
      "Boot_Start_Delay": ""
    },
    {
      "Number": 7,
      "Name": "",
      "Enable": True,
      "Link": "Auto",
      "PoE": "48V",
      "FlowControl": "Both",
      "Multicast": True,
      "MTU": "1528",
      "TxLimit": "",
      "RxLimit": "",
      "STP": True,
      "STPPriority": "128",
      "STP_Path_Cost": "",
      "Stats": True,
      "Isolation": False,
      "AllowedVLANs": "",
      "DHCP_Snooping": False,
      "Shutdown_Voltage": "",
      "Restart_Voltage": "",
      "Priority": "7",
      "Shutdown_Time": "",
      "Startup_Time": "",
      "Updated_SFP2": True,
      "QoSSched": "Strict",
      "PoE_Smart": True,
      "Updated_MTU": True,
      "Boot_Start_Delay": ""
    },
    {
      "Number": 8,
      "Name": "",
      "Enable": True,
      "Link": "Auto",
      "PoE": "48V",
      "FlowControl": "Both",
      "Multicast": True,
      "MTU": "1528",
      "TxLimit": "",
      "RxLimit": "",
      "STP": True,
      "STPPriority": "128",
      "STP_Path_Cost": "",
      "Stats": True,
      "Isolation": False,
      "AllowedVLANs": "",
      "DHCP_Snooping": False,
      "Shutdown_Voltage": "",
      "Restart_Voltage": "",
      "Priority": "8",
      "Shutdown_Time": "",
      "Startup_Time": "",
      "Updated_SFP2": True,
      "QoSSched": "Strict",
      "PoE_Smart": True,
      "Updated_MTU": True,
      "Boot_Start_Delay": ""
    },
    {
      "Number": 9,
      "Name": "",
      "Enable": True,
      "Link": "Auto",
      "PoE": "Off",
      "FlowControl": "Both",
      "Multicast": True,
      "MTU": "1528",
      "TxLimit": "",
      "RxLimit": "",
      "STP": True,
      "STPPriority": "128",
      "STP_Path_Cost": "",
      "Stats": True,
      "Isolation": False,
      "AllowedVLANs": "",
      "DHCP_Snooping": False,
      "Shutdown_Voltage": "",
      "Restart_Voltage": "",
      "Priority": "9",
      "Shutdown_Time": "",
      "Startup_Time": "",
      "Updated_SFP2": True,
      "QoSSched": "Strict",
      "PoE_Smart": True,
      "Updated_MTU": True,
      "Boot_Start_Delay": ""
    },
    {
      "Number": 10,
      "Name": "",
      "Enable": True,
      "Link": "Auto",
      "PoE": "Off",
      "FlowControl": "Both",
      "Multicast": True,
      "MTU": "1528",
      "TxLimit": "",
      "RxLimit": "",
      "STP": True,
      "STPPriority": "128",
      "STP_Path_Cost": "",
      "Stats": True,
      "Isolation": False,
      "AllowedVLANs": "",
      "DHCP_Snooping": False,
      "Shutdown_Voltage": "",
      "Restart_Voltage": "",
      "Priority": "10",
      "Shutdown_Time": "",
      "Startup_Time": "",
      "Updated_SFP2": True,
      "QoSSched": "Strict",
      "PoE_Smart": True,
      "Updated_MTU": True,
      "Boot_Start_Delay": ""
    },
    {
      "Number": 11,
      "Name": "",
      "Enable": True,
      "Link": "Auto",
      "PoE": "Off",
      "FlowControl": "Both",
      "Multicast": True,
      "MTU": "1528",
      "TxLimit": "",
      "RxLimit": "",
      "STP": True,
      "STPPriority": "128",
      "STP_Path_Cost": "",
      "Stats": True,
      "Isolation": False,
      "AllowedVLANs": "",
      "DHCP_Snooping": False,
      "Shutdown_Voltage": "",
      "Restart_Voltage": "",
      "Priority": "11",
      "Shutdown_Time": "",
      "Startup_Time": "",
      "Updated_SFP2": True,
      "QoSSched": "Strict",
      "PoE_Smart": True,
      "Updated_MTU": True,
      "Boot_Start_Delay": ""
    },
    {
      "Number": 12,
      "Name": "",
      "Enable": True,
      "Link": "Auto",
      "PoE": "Off",
      "FlowControl": "Both",
      "Multicast": True,
      "MTU": "1528",
      "TxLimit": "",
      "RxLimit": "",
      "STP": True,
      "STPPriority": "128",
      "STP_Path_Cost": "",
      "Stats": True,
      "Isolation": False,
      "AllowedVLANs": "",
      "DHCP_Snooping": False,
      "Shutdown_Voltage": "",
      "Restart_Voltage": "",
      "Priority": "12",
      "Shutdown_Time": "",
      "Startup_Time": "",
      "Updated_SFP2": True,
      "QoSSched": "Strict",
      "PoE_Smart": True,
      "Updated_MTU": True,
      "Boot_Start_Delay": ""
    },
    {
      "Number": 13,
      "Name": "",
      "Enable": True,
      "Link": "Auto",
      "PoE": "Off",
      "FlowControl": "Both",
      "Multicast": True,
      "MTU": "1528",
      "TxLimit": "",
      "RxLimit": "",
      "STP": True,
      "STPPriority": "128",
      "STP_Path_Cost": "",
      "Stats": True,
      "Isolation": False,
      "AllowedVLANs": "",
      "DHCP_Snooping": False,
      "Shutdown_Voltage": "",
      "Restart_Voltage": "",
      "Priority": "13",
      "Shutdown_Time": "",
      "Startup_Time": "",
      "Updated_SFP2": True,
      "QoSSched": "Strict",
      "PoE_Smart": True,
      "Updated_MTU": True,
      "Boot_Start_Delay": ""
    },
    {
      "Number": 14,
      "Name": "",
      "Enable": True,
      "Link": "Auto",
      "PoE": "Off",
      "FlowControl": "Both",
      "Multicast": True,
      "MTU": "1528",
      "TxLimit": "",
      "RxLimit": "",
      "STP": True,
      "STPPriority": "128",
      "STP_Path_Cost": "",
      "Stats": True,
      "Isolation": False,
      "AllowedVLANs": "",
      "DHCP_Snooping": False,
      "Shutdown_Voltage": "",
      "Restart_Voltage": "",
      "Priority": "14",
      "Shutdown_Time": "",
      "Startup_Time": "",
      "Updated_SFP2": True,
      "QoSSched": "Strict",
      "PoE_Smart": True,
      "Updated_MTU": True,
      "Boot_Start_Delay": ""
    }
  ],
  "LACP": [
    {
      "Port": 1,
      "Enable": False,
      "Key": "",
      "Role": "Active",
      "Timeout": "Fast",
      "Priority": 32768
    },
    {
      "Port": 2,
      "Enable": False,
      "Key": "",
      "Role": "Active",
      "Timeout": "Fast",
      "Priority": 32768
    },
    {
      "Port": 3,
      "Enable": False,
      "Key": "",
      "Role": "Active",
      "Timeout": "Fast",
      "Priority": 32768
    },
    {
      "Port": 4,
      "Enable": False,
      "Key": "",
      "Role": "Active",
      "Timeout": "Fast",
      "Priority": 32768
    },
    {
      "Port": 5,
      "Enable": False,
      "Key": "",
      "Role": "Active",
      "Timeout": "Fast",
      "Priority": 32768
    },
    {
      "Port": 6,
      "Enable": False,
      "Key": "",
      "Role": "Active",
      "Timeout": "Fast",
      "Priority": 32768
    },
    {
      "Port": 7,
      "Enable": False,
      "Key": "",
      "Role": "Active",
      "Timeout": "Fast",
      "Priority": 32768
    },
    {
      "Port": 8,
      "Enable": False,
      "Key": "",
      "Role": "Active",
      "Timeout": "Fast",
      "Priority": 32768
    },
    {
      "Port": 9,
      "Enable": False,
      "Key": "",
      "Role": "Active",
      "Timeout": "Fast",
      "Priority": 32768
    },
    {
      "Port": 10,
      "Enable": False,
      "Key": "",
      "Role": "Active",
      "Timeout": "Fast",
      "Priority": 32768
    },
    {
      "Port": 11,
      "Enable": False,
      "Key": "",
      "Role": "Active",
      "Timeout": "Fast",
      "Priority": 32768
    },
    {
      "Port": 12,
      "Enable": False,
      "Key": "",
      "Role": "Active",
      "Timeout": "Fast",
      "Priority": 32768
    },
    {
      "Port": 13,
      "Enable": False,
      "Key": "",
      "Role": "Active",
      "Timeout": "Fast",
      "Priority": 32768
    },
    {
      "Port": 14,
      "Enable": False,
      "Key": "",
      "Role": "Active",
      "Timeout": "Fast",
      "Priority": 32768
    }
  ],
  "VLANs": [
    {
      "ID": "4000",
      "Name": "Management",
      "Enable": True,
      "PortSettings": "UUUUUUUUUUUUUU",
      "IPv4_Enable": False,
      "IPv4_Address": "",
      "IPv4_Netmask": "",
      "IPv6_Enable": False,
      "IPv6_Address": "",
      "IGMP_Querier": False
    },
    {
      "PortSettings": "TTTTTTTTTTTTTT",
      "Enable": True,
      "Name": "1100",
      "ID": "1100",
      "IPv4_Enable": False,
      "IPv4_Address": "",
      "IPv4_Netmask": "",
      "IPv6_Enable": False,
      "IPv6_Address": "",
      "IGMP_Querier": True
    },
    {
      "PortSettings": "TTTTTTTTTTTTTT",
      "Enable": True,
      "Name": "1110",
      "ID": "1110",
      "IPv4_Enable": False,
      "IPv4_Address": "",
      "IPv4_Netmask": "",
      "IPv6_Enable": False,
      "IPv6_Address": "",
      "IGMP_Querier": True
    },
    {
      "PortSettings": "TTTTTTTTTTTTTT",
      "Enable": True,
      "Name": "1120",
      "ID": "1120",
      "IPv4_Enable": False,
      "IPv4_Address": "",
      "IPv4_Netmask": "",
      "IPv6_Enable": False,
      "IPv6_Address": "",
      "IGMP_Querier": True
    },
    {
      "PortSettings": "TTTTTTTTTTTTTT",
      "Enable": True,
      "Name": "1130",
      "ID": "1130",
      "IPv4_Enable": False,
      "IPv4_Address": "",
      "IPv4_Netmask": "",
      "IPv6_Enable": False,
      "IPv6_Address": "",
      "IGMP_Querier": True
    },
    {
      "PortSettings": "TTTTTTTTTTTTTT",
      "Enable": True,
      "Name": "1140",
      "ID": "1140",
      "IPv4_Enable": False,
      "IPv4_Address": "",
      "IPv4_Netmask": "",
      "IPv6_Enable": False,
      "IPv6_Address": "",
      "IGMP_Querier": True
    },
    {
      "PortSettings": "TTTTTTTTTTTTTT",
      "Enable": True,
      "Name": "1150",
      "ID": "1150",
      "IPv4_Enable": False,
      "IPv4_Address": "",
      "IPv4_Netmask": "",
      "IPv6_Enable": False,
      "IPv6_Address": "",
      "IGMP_Querier": True
    },
    {
      "PortSettings": "TTTTTTTTTTTTTT",
      "Enable": True,
      "Name": "1160",
      "ID": "1160",
      "IPv4_Enable": False,
      "IPv4_Address": "",
      "IPv4_Netmask": "",
      "IPv6_Enable": False,
      "IPv6_Address": "",
      "IGMP_Querier": True
    },
    {
      "PortSettings": "TTTTTTTTTTTTTT",
      "Enable": True,
      "Name": "1170",
      "ID": "1170",
      "IPv4_Enable": False,
      "IPv4_Address": "",
      "IPv4_Netmask": "",
      "IPv6_Enable": False,
      "IPv6_Address": "",
      "IGMP_Querier": True
    },
    {
      "PortSettings": "TTTTTTTTTTTTTT",
      "Enable": True,
      "Name": "1180",
      "ID": "1180",
      "IPv4_Enable": False,
      "IPv4_Address": "",
      "IPv4_Netmask": "",
      "IPv6_Enable": False,
      "IPv6_Address": "",
      "IGMP_Querier": True
    },
    {
      "PortSettings": "TTTTTTTTTTTTTT",
      "Enable": True,
      "Name": "1190",
      "ID": "1190",
      "IPv4_Enable": False,
      "IPv4_Address": "",
      "IPv4_Netmask": "",
      "IPv6_Enable": False,
      "IPv6_Address": "",
      "IGMP_Querier": True
    },
    {
      "PortSettings": "TTTTTTTTTTTTTT",
      "Enable": True,
      "Name": "1200",
      "ID": "1200",
      "IPv4_Enable": False,
      "IPv4_Address": "",
      "IPv4_Netmask": "",
      "IPv6_Enable": False,
      "IPv6_Address": "",
      "IGMP_Querier": True
    }
  ],
  "Mirror": {
    "Port": "None",
    "RemoteHost": "",
    "Filter_MAC": "",
    "Filter_IP": "",
    "Ports": []
  },
  "Auto_Backup_Enable": False,
  "Syslog_Log_Logins": False,
  "Options_MAC_Aging": "300",
  "MSTP_Name": "",
  "MSTP_Revision": 0,
  "MSTI": [
    {
      "Priority": "32768",
      "VLAN_List": "",
      "Ports": [
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        }
      ]
    },
    {
      "Priority": "32768",
      "VLAN_List": "",
      "Ports": [
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        }
      ]
    },
    {
      "Priority": "32768",
      "VLAN_List": "",
      "Ports": [
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        }
      ]
    },
    {
      "Priority": "32768",
      "VLAN_List": "",
      "Ports": [
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        }
      ]
    },
    {
      "Priority": "32768",
      "VLAN_List": "",
      "Ports": [
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        }
      ]
    },
    {
      "Priority": "32768",
      "VLAN_List": "",
      "Ports": [
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        }
      ]
    },
    {
      "Priority": "32768",
      "VLAN_List": "",
      "Ports": [
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        },
        {
          "Priority": "128",
          "Path_Cost": ""
        }
      ]
    }
  ],
  "ERPS": [],
  "MEPs": [],
  "SNMP_Server_Version_2c": True,
  "SNMP_Server_Version_1": False,
  "Syslog_Log_Name": False,
  "Discovery_Broadcast_On_Protocols": True
}


class TestMergeConfigMethods(unittest.TestCase):
    def test_merge_by_key(self):
        data = [
            {
                "Number": "1",
                "value1": "a1",
                "value2": "a2",
            },
            {
                "Number": "2",
                "value1": "b1",
                "value2": "b2",
            },
            {
                "Number": "1",
                "value1": "c1",
                "value2": "c2",
            }
        ]
        data_orig = data.copy()
        Netonix._merge_by_key(
            data,
            [
                {
                    "Number": "2",
                    "value1": "a1",
                    "value": "a"
                }
            ]
        )
        for i in [0, 2]:
            for a in data[i].keys():
                self.assertEqual(data[0][a], data_orig[0][a])
        self.assertEqual(data[1]["Number"], "2")
        self.assertEqual(data[1]["value1"], "a1")
        self.assertEqual(data[1]["value2"], "b2")
        self.assertEqual(data[1]["value"], "a")


class TestMergeConfig(unittest.TestCase):
    def test_mergeConfig(self):
        config_new = {}
        config_new["Discovery_Ubiquiti"] = "GG"
        config_new["MEPs"] = ["a", "b"]
        config_new["Ports"] = [
            {
              "Number": 5,
              "Name": "TEST1",
              "Enable": False,
            }
        ]
        self.n = Netonix()
        self.n.config = get_test_config()
        self.n.mergeConfig(config_new)

        for k, v in config_new.items():
            if(k == "Ports"):
                for a in self.n.config[k]:
                    if(a["Number"] == 5):
                        self.assertEqual(a["Name"], "TEST1")
                        self.assertEqual(a["Enable"], False)
                continue
            self.assertEqual(self.n.config[k], v)


if __name__ == '__main__':
    unittest.main()
