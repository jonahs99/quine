s = 's = \'*\'; print(s.replace(\'*\', s.replace(\'\\\\\', \'\\\\\\\\\').replace(\'\\\'\', \'\\\\\\\'\'), 1))'; print(s.replace('*', s.replace('\\', '\\\\').replace('\'', '\\\''), 1))
