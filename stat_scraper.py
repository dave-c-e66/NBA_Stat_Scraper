# Author: David Elrick
# Date: July 22, 2022
# Description: The program scrapes the website

import requests, bs4, time


def get_salary_data():
    """When called this function returns a dictionary that contains the NBA player names as keys
    and their salary's as the values"""

    web_addr = requests.get('https://www.basketball-reference.com/contracts/players.html').text
    soup = bs4.BeautifulSoup(web_addr,'lxml')
    salary_table = soup.find('table',id="player-contracts")  # grab the table we are looking for from the website
    table_body = salary_table.find('tbody') # get the body of the table that has the values we are looking for
    salary_dict = {}
    rows = table_body.find_all('tr')  # this will put all table rows tr into variable rows
    # iterate over the rows in the table, strip off the extra text and get the names and salarys
    for row in rows:
        name=""
        salary=""
        coloumns = row.find_all('td')
        coloumns = [ele.text.strip() for ele in coloumns]
        i=0
        for entry in coloumns:
            if i==0: # the first item is the name
                name = entry
            elif i ==2: # the third item is the salary
                salary = entry
            i+=1
        salary_dict[name] = salary   # add each player name and their salary to the dictionary
    return salary_dict

def get_player_name():
    """ opens up fiel player_name.txt and returns the name of the nba player found there"""
    with open('player_name.txt', 'r', encoding="utf-8") as file:
        player_name = file.read()
    file = open('player_name.txt', 'w', encoding="utf-8") # this deletes existing file so it can be used again
    file.close()
    return player_name

def write_salary(salary):
    """ write the salary provided to the file player_salary.txt"""
    with open('player_salary.txt', 'w', encoding="utf-8") as file:  # this deletes existing file and creates new one
        file.write(salary)


def main():

    salary_dict = get_salary_data() #create dictionary Key: players name Item: their salary
    while True:
        player_name = get_player_name()
        if len(player_name) > 0:          # check if a name was written if so length will be greater then 0
            write_salary(salary_dict[player_name])
        time.sleep(3)

if __name__ == '__main__':  main()   # run main only if this file is run directly