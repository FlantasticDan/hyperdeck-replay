from telnetlib import Telnet
from threading import Thread

class Hyperdeck:
    def __init__(self, ip_address, id) -> None:
        self.deck = Telnet(ip_address, 9993)
        self.id = id

        self.thread = Thread(target=self.listener)
        self.thread.start()

    
    def listener(self):
        while True:
            message = self.deck.read_some()
            print(f'//{self.id}//')
            print(message)
    
    def identify_standard_command(self, command, recording=0):
        if command == 'live':
            return 'preview: enable: true'
        elif command == 'clip':
            return 'preview: enable: false\r\nplayrange clear'
        elif command == 'record':
            return f'record: name: {self.id}{recording}'
        elif command == 'play':
            return 'play: single clip: true'
        elif command == 'stop':
            return 'stop'
        elif command == 'previous':
            return 'goto: clip id: -1'
        elif command == 'next':
            return 'goto: clip id: +1'
        elif command == 'beginning':
            return 'goto: clip: start'
        elif command == 'end':
            return 'goto: clip: end'

    def identify_granular_command(self, command, direction):
        if direction == 'forward':
            sign = '+'
        else:
            sign = '-'
        
        if command == '10%':
            return f'play: single clip: true speed: {sign}10'
        elif command == '25%':
            return f'play: single clip: true speed: {sign}25'
        elif command == '50%':
            return f'play: single clip: true speed: {sign}50'
        elif command == '75%':
            return f'play: single clip: true speed: {sign}75'
        elif command == '10s':
            return f'jog: timecode: {sign}00:00:10:00'
        elif command == '5s':
            return f'jog: timecode: {sign}00:00:05:00'
        elif command == '1s':
            return f'jog: timecode: {sign}00:00:01:00'
        elif command == '1f':
            return f'jog: timecode: {sign}00:00:00:01'
    
    def send_standard_command(self, command, recording=0):
        identified_command = self.identify_standard_command(command, recording)
        query = bytes(f'{identified_command}\r\n', 'ascii')
        self.deck.write(query)
    
    def send_granular_command(self, command, direction):
        identified_command = self.identify_granular_command(command, direction)
        query = bytes(f'{identified_command}\r\n', 'ascii')
        self.deck.write(query)
    