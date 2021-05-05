# Pyinstaller Spec File
```python
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['flask'],
             binaries=[],
             datas=[('templates', 'templates'), ('static', 'static')],
             hiddenimports=[
                 'engineio.async_drivers.eventlet',
                 'eventlet.hubs.epolls',
                 'eventlet.hubs.kqueue',
                 'eventlet.hubs.selects',
                 'dns.dnssec',
                 'dns.e164',
                 'dns.hash',
                 'dns.namedict',
                 'dns.tsigkeyring',
                 'dns.update',
                 'dns.version',
                 'dns.zone'
                 ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Hyperdeck-Replay-v#.#.#',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
```