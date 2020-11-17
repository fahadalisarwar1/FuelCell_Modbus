from pymodbus.client.sync import ModbusTcpClient as ModbusClient
UNIT = 0x1
if __name__ == '__main__':
    client = ModbusClient("192.168.2.205", port=502)
    # connected = client.connect()

    try:
        # if connected:
        #     print("[+] Connection Status:\t", connected)
        reg = 101
        num_regs = 1
        rr = client.read_holding_registers(reg, num_regs, unit=UNIT)
        print("[+] Reg:\t", reg,"\tvalue:\t", rr)
    except Exception as conn_err:
        print(conn_err)

