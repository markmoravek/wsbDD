# wsbDD
Automatically does the "due diligence" for you. 

If you want to know what stocks people are talking about in r/wallstreetbets over 
at Reddit, this is the tool for you. 

## Installation
There is a ``Pipfile`` for pipenv, if you are into that. It was automatically 
generated by Pycham. I personally simply installed ``psaw`` in my Python 
environment

## Running
Simply type in:

    For 24 hour DD:	
    python3 wsbDD24.py

    For 7 day DD:
    python3 wsb7.py 

It will output the most frequently discussed tickers in
r/wallstreetbets into a .csv file

## Example output

    Code    Frequency
    MVIS    198
    IZEA    106
    KTOV    30
    RTTR    30
    MARK    21
    GNUS    12
    MSFT    12
    INUV    11
    DECN    11
    TTI     10
    UAVS    10
    ...

## License

    AutoDD - Automatically does the "due diligence" for you. 
    Copyright (C) 2020  Fufu Fang

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
