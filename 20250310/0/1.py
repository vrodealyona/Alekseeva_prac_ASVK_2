import shlex
import cmd
import calendar

Months = {'JANUARY' : 1, 'FEBRUARY' : 2, 'MARCH' : 3,
    'APRIL' : 4,
    'MAY' : 5,
    'JUNE' : 6,
    'JULY' : 7,
    'AUGUST' : 8,
    'SEPTEMBER' : 9,
    'OCTOBER' : 10,
    'NOVEMBER' : 11,
    'DECEMBER' : 12}


class calend(cmd.Cmd):
    prompt = "cmd>> "
    
    def do_pryear(self, theyear):
        "Print the calendar for an entire year as returned "
        calendar.TextCalendar().pryear(int(theyear))
		
    def do_prmonth(self, the):
        "Print a month’s calendar as returned"
        theyear, themonth = shlex.split(the)
        calendar.TextCalendar().prmonth(int(theyear), int(themonth))
        
    def complete_number(self, text, line, begidx, endidx):
        words = (line[:endidx] + ".").split()
        return [c for c in Months if c.startswith(text)]
        
    def do_EOF(self, arg):
        return 1

if __name__ == '__main__':
    calend().cmdloop() 
