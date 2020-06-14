#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" redditTickerCounter.py - count the number of stock ticker mentions in a
subreddit

Copyright (C) 2020  Fufu Fang
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; w\without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from reddit_regex_counter.redditRegexCounter import SubmissionCounter, \
    CommentCounter
from tickerValidator import NASDAQTickerValidator
from datetime import date
import pandas as pd

def print_ticker_count24(tbl):
    """ print a ticker count table. 
    
    :param tbl: the input dictionary with ticker count
    :return: a string containing the formatted output
    """

    #create file
    today = date.today()
    filename = f'wsbDD24_{today}.txt'

    #populate
    s = "Ticker:\tCount:\n"
    for i in tbl.items():
        s += str(i[0]) + "\t" + str(i[1]) + "\n"

    #print in cmd?
    #print(s)

    #print to file
    with open(filename, 'w') as file_object:
        file_object.write(s)
    df = pd.read_csv(filename,delimiter= "\t")
    df.to_csv(f'wsbDD24_{today}.csv', index=False)

    print(f'\nwsbdd24_{today}.csv created in current folder\n')

def print_ticker_count7(tbl):
    """ print a ticker count table. 
    
    :param tbl: the input dictionary with ticker count
    :return: a string containing the formatted output
    """

    #create file
    today = date.today()
    filename = f'wsbDD7_{today}.txt'

    #populate
    s = "Ticker:\tCount:\n"
    for i in tbl.items():
        s += str(i[0]) + "\t" + str(i[1]) + "\n"

    #print in cmd?
    #print(s)

    #print to file
    with open(filename, 'w') as file_object:
        file_object.write(s)
    df = pd.read_csv(filename,delimiter= "\t")
    df.to_csv(f'wsbDD7_{today}.csv', index=False)

    print(f'\nwsbdd7_{today}.csv created in current folder\n')
    

def count_subreddit_ticker(s_name, s_time, e_time, dbfn, result=None, debug=0):
    """ count the stock ticker mention in a subreddit.

    :param s_name: subreddit name
    :param s_time: start time as a datetime object
    :param e_time: end time as a datetime object
    :param dbfn:  backing file which stores the ticker database
    :param result: optionally result table from a previous run - the results
                from a new run will be added to this table
    :param debug: whether we get the TickerValidator to print debug messages
    :return: a dictionary containing the the number of mentions of each valid
            ticker symbol
    """
    if result is None:
        result = {}
    pattern = r"\b[A-Z]{3,5}\b"
    s_counter = SubmissionCounter(s_name, s_time, e_time, pattern, case=1,
                                  result=result)
    s_counter.get_result()
    c_counter = CommentCounter(s_name, s_time, e_time, pattern, case=1,
                               result=s_counter.result)
    c_counter.get_result()

    validator = NASDAQTickerValidator(dbfn, debug)
    result = validator.validate_dict(c_counter.result)
    return result
