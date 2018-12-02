#!/usr/bin/env python

"""
Kamina is an alternative Internet platform to the Web

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import sys, multiprocessing
from datetime import date, datetime, timedelta
from multiprocessing import Process

import click

import secretary
from manager import Manager
from desk import Desk


class Kamina:
    def __init__(self):
        self.staff = []
        self.office = [Desk(False)]
        self.log = secretary.hire( "Kamina", debug=True, logfile=\
                    ("run" + datetime.now().strftime('%y%m%d') + ".log") )
        
    def run(self):
        manager = Manager(debug=True, desk=self.office[0])
        m = Process(target=Manager.run, args=(manager,))
        m.daemon = True; m.start()
        self.staff.append(m)
        
        for m in self.staff:  m.join()


@click.command()
def main():
    self = Kamina()
    
    self.run()

if __name__ == "__main__":
    main()
