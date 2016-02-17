#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

def getTextFilePOICount():
	import re

	f = open('../final_project/poi_names.txt', 'r')
	p = re.compile('\([yn]\)\s(.+)$')

	return sum([1 for line in f if p.search(line)])

def getEmailAdresses():
	import sys
	sys.path.insert(0, './../final_project/')
	from poi_email_addresses import poiEmails

	return poiEmails()

def getEnronDatasetPOICount(enron_data):
	return sum([1 for name in enron_data if enron_data[name]['poi'] == True])

def getQuantifiedSalaryCount(enron_data):
	return sum([1 for name in enron_data if enron_data[name]['salary'] != 'NaN'])

def getKnownEmailAddressesCount(enron_data):
	return sum([1 for name in enron_data if enron_data[name]['email_address'] != 'NaN'])

def getPeopleWithoutTotalPaymentsCount(enron_data):
	return sum([1 for name in enron_data if enron_data[name]['total_payments'] == 'NaN'])

def getPOIWithoutTotalPaymentsCount(enron_data):
	return sum([1 for name in enron_data if enron_data[name]['total_payments'] == 'NaN' and enron_data[name]['poi'] == True])

total = len(enron_data)
poi_total = getEnronDatasetPOICount(enron_data)

without_payments_count = getPeopleWithoutTotalPaymentsCount(enron_data)
without_payments_percentage = without_payments_count * 100.0/total

poi_without_payments_count = getPOIWithoutTotalPaymentsCount(enron_data)
poi_without_payments_percentage = poi_without_payments_count * 100.0/poi_total

print "Size of dataset: ", total
print "Number of features per entry: ", len(enron_data.itervalues().next())
print "Number of POI: ", poi_total
print "Number of POI in 'poi_names.txt': ", getTextFilePOICount()
print "Total stock value of James Prentice: ", enron_data['PRENTICE JAMES']['total_stock_value']
print "Messages from Wesley Colwell to POIs: ", enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print "Value of stock option exercised by Jeffrey Skilling: ", enron_data['SKILLING JEFFREY K']['exercised_stock_options']
print "Lay total payments", enron_data['LAY KENNETH L']['total_payments']
print "Jeff total payments", enron_data['SKILLING JEFFREY K']['total_payments']
print "Andrew total payments", enron_data['FASTOW ANDREW S']['total_payments']
print "Folks with quantified salary: ", getQuantifiedSalaryCount(enron_data)
print "Known email addresses: ", getKnownEmailAddressesCount(enron_data)
print "People with total payments not specified: %s (%s%%)" % (without_payments_count, without_payments_percentage)
print "POI with total payments not specified: %s (%s%%)" % (poi_without_payments_count, poi_without_payments_percentage)
