#!/usr/bin/env python

"""
A simple python script template.
"""

from __future__ import print_function, unicode_literals
from pymongo import MongoClient
from PyInquirer import prompt
from pprint import pprint
from collections import Iterable

import os
import sys
import argparse
import datetime

## Main
def main(arguments):

    ## connecting to the database and defining database and collection
    client = MongoClient('mongodb://ec2-52-53-221-67.us-west-1.compute.amazonaws.com:27023/')
    db=client.vparkdb
    tickets = db.vpark
    
    ## prompting user for choice
    while True:
        answers = promptUser()
        if 'choice' in answers:

            #1
            if answers.get('choice') == 'insert':
                printResult('Inserted ticket id', promptInsert(tickets))

            #2
            if answers.get('choice') == 'read':
                printResult('Ticket information', list(promptRead(tickets)))

            #3
            if answers.get('choice') == 'update':
                printResult('Updated information', promptUpdate(tickets))

            #4
            if answers.get('choice') == 'delete':
                printResult('Deleted ticket id', promptDelete(tickets))

            #5
            if answers.get('choice') == 'searchByState':
                printResult('Tickets from state', list(promptSearchByState(tickets)))

            #6
            if answers.get('choice') == 'searchByTimeRange':
                printResult('Tickets by range (time)', list(promptSearchByTimeRange(tickets)))

            #7
            if answers.get('choice') == 'searchByMakeModel':
                printResult('Tickets by make/model', list(promptSearchByMakeModel(tickets)))

            #8
            if answers.get('choice') == 'searchByStreet':
                printResult('Tickets by street (fuzzy search)', list(promptSearchByStreet(tickets)))

            #9
            if answers.get('choice') == 'searchByAgency':
                printResult('Tickets by agency number', list(promptSearchByAgency(tickets)))

            #10
            if answers.get('choice') == 'searchAverageByYear':
                printResult('Average for specific year', list(promptSearchAverageByYear(tickets)))

            #11
            if answers.get('choice') == 'searchViolationTypes':
                printResult('List of violation types', list(promptSearchViolationTypes(tickets)))

            #12
            if answers.get('choice') == 'searchSumOfFinesByYear':
                printResult('Sum of fines by year', list(promptSearchSumOfFinesByYear(tickets)))

            #13
            if answers.get('choice') == 'searchSumOfFinesByMonth':
                printResult('Sum of fines by month', list(promptSearchSumOfFinesByMonth(tickets)))

            #14
            if answers.get('choice') == 'searchTicketNumberByMake':
                printResult('Total number of tickets by make', promptSearchTicketNumberByMake(tickets))
            
            #15       
            if answers.get('choice') == 'searchByOverTime':
                printResult('List the tickets ', list(promptSearchByOverTime(tickets)))
            
            #16    
            if answers.get('choice') == 'sample':
                printResult('Sample of dataset', list(promptSample(tickets)))

            #17
            if answers.get('choice') == 'exit':
                break

    # pprint(answers)

## User menu 
def promptUser():

    ## Questions definition
    questions = [
        {
            'type': 'list',
            'name': 'choice',
            'message': 'What would you like to do?',
            'choices':[
                {
                    'key': '1',
                    'name': 'Insert a ticket',
                    'value': 'insert'
                },
                {
                    'key': '2',
                    'name': 'Seach a ticket',
                    'value': 'read'
                },
                {
                    'key': '3',
                    'name': 'Update a ticket',
                    'value': 'update'
                },
                {
                    'key': '4',
                    'name': 'Delete a ticket',
                    'value': 'delete'
                },
                 {
                    'key': '5',
                    'name': 'Search ticket by state',
                    'value': 'searchByState'
                },
                {
                    'key': '6',
                    'name': 'Search within a time range',
                    'value': 'searchByTimeRange'
                },
                {
                    'key': '7',
                    'name': 'Search by make/model',
                    'value': 'searchByMakeModel'
                },
                {
                    'key': '8',
                    'name': 'Search by street (fuzzy search)',
                    'value': 'searchByStreet'
                },
                {
                    'key': '9',
                    'name': 'Search by agency',
                    'value': 'searchByAgency'
                },
                {
                    'key': '10',
                    'name': 'Average fine amount in specific year',
                    'value': 'searchAverageByYear'
                },
                {
                    'key': '11',
                    'name': 'List different type of violations',
                    'value': 'searchViolationTypes'
                },
                {
                    'key': '12',
                    'name': 'Sum of fine amount in specific year',
                    'value': 'searchSumOfFinesByYear'
                },
                {
                    'key': '13',
                    'name': 'Sum of fine amount in specific month',
                    'value': 'searchSumOfFinesByMonth'
                },
                {
                    'key': '14',
                    'name': 'Find the total number of tickets issued to a specific make of car',
                    'value': 'searchTicketNumberByMake'
                },
                {
                    'key': '15',
                    'name': 'List of all the tickets that are due to being parked over time',
                    'value': 'searchByOverTime'
                },
                {
                    'key': '16',
                    'name': 'Visualize a sample of dataset',
                    'value': 'sample'
                },
                {
                    'key': '0',
                    'name': 'Exit program',
                    'value': 'exit'
                },

            ],
            # 'filter': lambda val: val.lower()
        }
    ]

    return prompt(questions)

## 1 Inserting a ticket
def promptInsert( tickets ):

    ## Questions definition
    questions = [
        {
            'type': 'input',
            'name': 'ticket_number',
            'message': 'Leave the following question empty for default values.  Enter new ticket number to INSERT:',
            'default': '500000'
        },
        {
            'type': 'input',
            'name': 'issue_date',
            'message': 'Enter the issue date:',
            'default': '2018-02-05T00:00:00'
        },
        {
            'type': 'input',
            'name': 'issue_time',
            'message': 'Enter the issue date:',
            'default': '1216.0'
        },
        {
            'type': 'input',
            'name': 'rp_state_plate',
            'message': 'Enter the state plate number:',
            'default': 'CA'
        },
        {
            'type': 'input',
            'name': 'plate_expiry_date',
            'message': 'Enter the plate experiation date:',
            'default': '201807.0'
        },
        {
            'type': 'input',
            'name': 'make',
            'message': 'Enter the car make:',
            'default': 'NISS'
        },
        {
            'type': 'input',
            'name': 'body_style',
            'message': 'Enter the car body style:',
            'default': 'PA'
        },
        {
            'type': 'input',
            'name': 'color',
            'message': 'Enter the car color:',
            'default': 'BK'
        },
        {
            'type': 'input',
            'name': 'location',
            'message': 'Enter the violation location:',
            'default': '750 SPAULDING AVE S"'
        },
        {
            'type': 'input',
            'name': 'route',
            'message': 'Enter the route:',
            'default': '00144.0'
        },
        {
            'type': 'input',
            'name': 'agency',
            'message': 'Enter the agency number:',
            'default': '51.0'
        },
        {
            'type': 'input',
            'name': 'violation_code',
            'message': 'Enter the violation code:',
            'default': '80.69BS'
        },
        {
            'type': 'input',
            'name': 'violation_description',
            'message': 'Enter the violation description:',
            'default': 'NO PARK/STREET CLEAN'
        },
        {
            'type': 'input',
            'name': 'fine_amount',
            'message': 'Enter the fine amount:',
            'default': '73.0'
        },
        {
            'type': 'input',
            'name': 'latitude',
            'message': 'Enter the latitude:',
            'default': '6453238.3586370004'
        },
        {
            'type': 'input',
            'name': 'longitude',
            'message': 'Enter the longitude:',
            'default': '844996.969673'
        }
    ]

    ## prompt user with questions
    answers = prompt(questions)
    
    ## Gather user answers
    ticket_data = {
        "Ticket number": float(answers.get('ticket_number')),
        "Issue Date": answers.get('issue_date'),
        "Issue time": float(answers.get('issue_time')),
        "RP State Plate": answers.get('rp_state_plate'),
        "Plate Expiry Date": float(answers.get('plate_expiry_date')),
        "Make": answers.get('make'),
        "Body Style": answers.get('body_style'),
        "Color": answers.get('color'),
        "Location": answers.get('location'),
        "Route": answers.get('route'),
        "Agency": float(answers.get('agency')),
        "Violation code": answers.get('violation_code'),
        "Violation Description": answers.get('violation_description'),
        "Fine amount": float(answers.get('fine_amount')),
        "Latitude": float(answers.get('latitude')),
        "Longitude": float(answers.get('longitude'))
    }

    ## Insert ticket in ticket collection
    return tickets.insert_one(ticket_data)

## 2 Looking for ticket by ticket number
def promptRead( tickets ):
    questions = [
        {
            'type': 'input',
            'name': 'ticket_number',
            'message': 'Enter ticket number to DISPLAY:',
            'default': '500000'
        }
    ]

    ## prompt user with questions
    answers = prompt(questions)

    return tickets.find({'Ticket number': float(answers.get('ticket_number'))})

## 3 Updating a ticket for ticket by ticket number
def promptUpdate( tickets ):
    questions = [
        {
            'type': 'input',
            'name': 'ticket_number',
            'message': 'Enter ticket number to UPDATE:',
            'default': '500000'
        }
    ]

    ## prompt user with questions
    answers = prompt(questions)

     ## Questions definition
    questions = [
        {
            'type': 'input',
            'name': 'ticket_number',
            'message': 'Enter new ticket number:',
            'default': '500000'
        },
        {
            'type': 'input',
            'name': 'issue_date',
            'message': 'Enter the issue date:',
            'default': '2018-02-05T00:00:00'
        },
        {
            'type': 'input',
            'name': 'issue_time',
            'message': 'Enter the issue date:',
            'default': '1216.0'
        },
        {
            'type': 'input',
            'name': 'rp_state_plate',
            'message': 'Enter the state plate number:',
            'default': 'CA'
        },
        {
            'type': 'input',
            'name': 'plate_expiry_date',
            'message': 'Enter the plate experiation date:',
            'default': '201807.0'
        },
        {
            'type': 'input',
            'name': 'make',
            'message': 'Enter the car make:',
            'default': 'NISS'
        },
        {
            'type': 'input',
            'name': 'body_style',
            'message': 'Enter the car body style:',
            'default': 'PA'
        },
        {
            'type': 'input',
            'name': 'color',
            'message': 'Enter the car color:',
            'default': 'BK'
        },
        {
            'type': 'input',
            'name': 'location',
            'message': 'Enter the violation location:',
            'default': '750 SPAULDING AVE S"'
        },
        {
            'type': 'input',
            'name': 'route',
            'message': 'Enter the route:',
            'default': '00144.0'
        },
        {
            'type': 'input',
            'name': 'agency',
            'message': 'Enter the agency number:',
            'default': '51.0'
        },
        {
            'type': 'input',
            'name': 'violation_code',
            'message': 'Enter the violation code:',
            'default': '80.69BS'
        },
        {
            'type': 'input',
            'name': 'violation_description',
            'message': 'Enter the violation description:',
            'default': 'NO PARK/STREET CLEAN'
        },
        {
            'type': 'input',
            'name': 'fine_amount',
            'message': 'Enter the fine amount:',
            'default': '73.0'
        },
        {
            'type': 'input',
            'name': 'latitude',
            'message': 'Enter the latitude:',
            'default': '6453238.3586370004'
        },
        {
            'type': 'input',
            'name': 'longitude',
            'message': 'Enter the longitude:',
            'default': '844996.969673'
        }
    ]

    ## prompt user with questions
    answers = prompt(questions)
    
    ## Set update variables
    updateFilter = {'Ticket number': float(answers.get('ticket_number'))}

    ## Gather user answers
    ticket_data = {
        "Ticket number": float(answers.get('ticket_number')),
        "Issue Date": answers.get('issue_date'),
        "Issue time": float(answers.get('issue_time')),
        "RP State Plate": answers.get('rp_state_plate'),
        "Plate Expiry Date": float(answers.get('plate_expiry_date')),
        "Make": answers.get('make'),
        "Body Style": answers.get('body_style'),
        "Color": answers.get('color'),
        "Location": answers.get('location'),
        "Route": answers.get('route'),
        "Agency": float(answers.get('agency')),
        "Violation code": answers.get('violation_code'),
        "Violation Description": answers.get('violation_description'),
        "Fine amount": float(answers.get('fine_amount')),
        "Latitude": float(answers.get('latitude')),
        "Longitude": float(answers.get('longitude'))
    }

    return tickets.update_one(updateFilter, {"$set": ticket_data})
 
## 4 Deleting a ticket by ticket number
def promptDelete( tickets ):
    questions = [
        {
            'type': 'input',
            'name': 'ticket_number',
            'message': 'Enter ticket number to DELETE:',
            'default': '500000'
        }
    ]

    ## prompt user with questions
    answers = prompt(questions)

    return tickets.delete_one({'Ticket number': float(answers.get('ticket_number'))})

## 5 List of all the tickets with a certain state plate
def promptSearchByState( tickets ):
    
    questions = [
        {
            'type': 'input',
            'name': 'plate_state',
            'message': 'Enter the state:',
            'default': 'CA'
        }
    ]

    ## prompt user with questions
    answers = prompt(questions)

    return tickets.find({'RP State Plate': answers.get('plate_state')})

## 6 List of all the tickets during a given time range
def promptSearchByTimeRange( tickets ):
    
    questions = [
        {
            'type': 'input',
            'name': 'time_start',
            'message': 'Enter the time range start:',
            'default': '1400'
        },
        {
            'type': 'input',
            'name': 'time_end',
            'message': 'Enter the time range end:',
            'default': '1500'
        }
    ]

    ## prompt user with questions
    answers = prompt(questions)

    return tickets.find({'Issue time': {'$gte' : float(answers.get('time_start')), '$lte': float(answers.get('time_end'))}})

## 7 List of all the tickets with a specific make/model of car
def promptSearchByMakeModel( tickets ):

    questions = [
        {
            'type': 'input',
            'name': 'make',
            'message': 'Enter the make of the car:',
            'default': 'BMW'
        }
    ]

    ## prompt user with questions
    answers = prompt(questions)

    return tickets.find({'Make': answers.get('make')})

## 8 List of all the tickets on a certain street
def promptSearchByStreet( tickets ):

    questions = [
        {
            'type': 'input',
            'name': 'street',
            'message': 'Enter the street address:',
            'default': 'CLOVERDALE'
        }
    ]

    ## prompt user with questions
    answers = prompt(questions)

    return tickets.find({'Location': {'$regex' : '.*' + answers.get('street') + '*.' }})

## 9 List of all the tickets of a specific agency
def promptSearchByAgency( tickets ):

    questions = [
        {
            'type': 'input',
            'name': 'agency',
            'message': 'Enter the agency number:',
            'default': '54'
        }
    ]

    ## prompt user with questions
    answers = prompt(questions)

    return tickets.find({'Agency': float(answers.get('agency'))})

    ## 9 List of all the tickets of a specific agency

## 10 Find the average fine amount in a certain year
def promptSearchAverageByYear( tickets ):
    
    questions = [
        {
            'type': 'input',
            'name': 'year',
            'message': 'Enter the year:',
            'default': '2018'
        }
    ]

    ## prompt user with questions
    answers = prompt(questions)

    pipeline = [
        { "$match" : { "Issue Date": { "$regex" : answers.get('year') + "-.*"}}},
        { "$group" : { "_id" : "null", "avgFine" : { "$avg" : "$Fine amount" }}}
    ]

    return tickets.aggregate(pipeline)

## 11 List the different types of violations (violation code or description of the violation)
def promptSearchViolationTypes( tickets ):

    return tickets.distinct('Violation Description')

## 12 Find the sum of the fines accumulated from a certain year
def promptSearchSumOfFinesByYear( tickets ):
    
    questions = [
        {
            'type': 'input',
            'name': 'year',
            'message': 'Enter the year:',
            'default': '2019'
        }
    ]

    ## prompt user with questions
    answers = prompt(questions)

    pipeline = [
        { "$match" : { "Issue Date": { "$regex" : answers.get('year') + "-.*"}}},
        { "$group" : { "_id" : "null", "fineSum" : { "$sum" : "$Fine amount" }}}
    ]

    return tickets.aggregate(pipeline)

## 13 Find the sum of fines issued from tickets from a certain month
def promptSearchSumOfFinesByMonth( tickets ):
   
    questions = [
        {
            'type': 'input',
            'name': 'month',
            'message': 'Enter the month:',
            'default': '05'
        }
    ]

    ## prompt user with questions
    answers = prompt(questions)

    pipeline = [
        { "$match" : { "Issue Date": { "$regex" : ".*-" + answers.get('month') + ".*" }}},
        { "$group" : { "_id" : "null", "fineSum" : { "$sum" : "$Fine amount" }}}
    ]

    return tickets.aggregate(pipeline)

## 14 Find the total number of tickets issued to a specific make of car
def promptSearchTicketNumberByMake( tickets ):
    
    questions = [
        {
            'type': 'input',
            'name': 'make',
            'message': 'Enter the make of the car:',
            'default': 'HOND'
        }
    ]

    ## prompt user with questions
    answers = prompt(questions)

    pipeline = [
        { '$match' : { 'Make': answers.get('make')}},
        { '$group' : { '_id' : 'Make', 'ticketCount' : { '$sum' : 1 }}}
    ]

    return tickets.aggregate(pipeline)
    
## 15 Find the average fine amount in a certain year
def promptSearchByOverTime( tickets ):
    
    questions = [
        {
            'type': 'input',
            'name': 'violation',
            'message': 'Enter the type of violation:',
            'default': 'PARKED OVER TIME LIMIT'
        }
    ]

    ## prompt user with questions
    answers = prompt(questions)

    return tickets.find({'Violation Description': answers.get('violation')})

## 16 Retrieving a sample data from db
def promptSample( tickets ):

    questions = [
        {
            'type': 'input',
            'name': 'sample_number',
            'message': 'Enter the number of samples:',
            'default': '10'
        }
    ]

    ## prompt user with questions
    answers = prompt(questions)

    pipeline = [
        { "$sample" : { "size": int(answers.get('sample_number'))}}
    ]

    return tickets.aggregate(pipeline)

## Giving feedback to user
def printResult( title, cursor ):

    count = 0

    try:
        ## checking if it is iterable
        iterator = iter(cursor)
    except TypeError, e:
        ## if it's not
        count += 1
        pprint('{0}: {1}'.format(title, cursor), indent = 4)
    else:
        ## if it is we iterate
        for doc in cursor:
            count += 1
            if count < 3:
                pprint('{0}:'.format(doc), indent = 4)
            if count == 3:
                pprint('...')
                pprint('(shortened for screenshots)')

    ## print total entries
    print('')
    print('-----------------------')
    pprint('Total entries: {0}'.format(count), indent = 4)
    print('-----------------------')

## connect to database
def dbConnect():
    client = MongoClient('localhost', 27017)
    return client.dataset


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))







