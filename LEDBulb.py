class LEDBulb:
  
    
    def __init__(self, ipaddr, port=55443):
      self.ipaddr = ipaddr
      self.port = port
      
    brightness = 0
    current_command_id = 0
    state = 0
      
    def operate_on_bulb(self, method, params):
      '''
      Operate on bulb; no gurantee of success.
      Input data 'params' must be a compiled into one string.
      E.g. params="1"; params="\"smooth\"", params="1,\"smooth\",80"
      '''
      #if idx not in bulb_idx2ip:
      #  print("error: invalid bulb idx")
      #  return
      
      bulb_ip = self.ipaddr
      port = self.port
      try:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("connect ",bulb_ip, port ,"...")
        tcp_socket.connect((bulb_ip, int(port)))
        msg="{\"id\":" + str(next_cmd_id()) + ",\"method\":\""
        msg += method + "\",\"params\":[" + params + "]}\r\n"
        tcp_socket.send(msg.encode())
        tcp_socket.close()
      except Exception as e:
        print("Unexpected error:", e)
        
      def next_cmd_id(self):
        self.current_command_id += 1
        return current_command_id


      
    def isOn(self):
      if state == 0:
        return False
      if state == 1:
        return True
        
    
    def turnOn(self):
      self.operate_on_bulb("set_power","on")
        
    def turnOff(self):
      self.operate_on_bulb("set_power","off")
      
    def setBrightness(self,brightness):
      self.brightness = brightness
      self.operate_on_bulb("bright",round(self.brightness/255*199))
    
    
    
