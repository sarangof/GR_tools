
import pandas as pd 
import os
import xlrd
import datetime
import numpy as np

def count_yes(word):
	return int(''.join(word.lower().split(' '))=='yes')

def update_demographics():
	"""
	Race = 
	age = #OJO: cambiar
	Offense = 
	SPIN_level = 
	Parent_institution = 
	Educational_level = 
	date_updated_demographics = 
	"""
	return None

def update_prerelease(prerelease_file):
	try: 
		workbook = xlrd.open_workbook(prerelease_file).sheet_by_index(0)
		ID = workbook.cell(3,2).value
		participant_name = workbook.cell(2, 2).value
		institution = workbook.cell(1, 2).value
		date_updated_prerelease_form = workbook.cell(5,2).value
		infractions_institution = workbook.cell(9,4).value
		tickets_institution = workbook.cell(10,4).value
		infractions_prerelease = workbook.cell(13,4).value
		tickets_prerelease = workbook.cell(14,4).value
		TFC_complete = workbook.cell(17, 4).value
		TFC_sessions = workbook.cell(16, 4).value
		partial_college_prerelase_1 = count_yes(workbook.cell(26,4).value)
		partial_college_prerelase_2 = count_yes(workbook.cell(27,4).value)
		partial_college_prerelase_3 = count_yes(workbook.cell(28,4).value)
		partial_college_prerelase_4 = count_yes(workbook.cell(29,4).value)
		partial_college_prerelase_total = partial_college_prerelase_1 + partial_college_prerelase_2 + partial_college_prerelase_3 + partial_college_prerelase_4
		GED_prerelease = workbook.cell(37,4).value
		certificate_programs_prerelease = workbook.cell(38,4).value
		birth_certificate = workbook.cell(31,4).value
		SS_card = workbook.cell(32,4).value
		ID_completion = workbook.cell(33,4).value
		resume = workbook.cell(34,4).value
		release_plan = workbook.cell(35,4).value
		prerelease_key = 1
		individual_prerelease = locals()
		del individual_prerelease['workbook'], individual_prerelease['prerelease_file']
		return pd.DataFrame(individual_prerelease, index=[ID])
	except xlrd.biffh.XLRDError:
		pass

def update_program(program_file):
	today_date = str(datetime.datetime.now().date())
	workbook = xlrd.open_workbook(program_file).sheet_by_index(0)
	program_key = 1
	ID = workbook.cell(3,2).value
	participant_name = workbook.cell(2, 2).value
	date_updated_program_form = datetime.datetime(*xlrd.xldate_as_tuple(workbook.cell(5,2).value, xlrd.open_workbook(program_file).datemode)).date()
	status_program = workbook.cell(6,2).value

	dynamic_variables = []

	if ''.join(workbook.cell(25,3).value.split(' ')).lower() == 'yes':
		incentive_program_1_cause = workbook.cell(25,4).value
		incentive_program_1_action = workbook.cell(25,5).value
		incentive_program_1_date = workbook.cell(25,6).value
		dynamic_variables.append([incentive_program_1_cause,incentive_program_1_action,incentive_program_1_date])
	
	if ''.join(workbook.cell(26,3).value.split(' ')).lower() == 'yes':
		incentive_program_2_cause = workbook.cell(26,4).value
		incentive_program_2_action = workbook.cell(26,5).value
		incentive_program_2_date = workbook.cell(26,6).value
		dynamic_variables.append([incentive_program_2_cause,incentive_program_2_action,incentive_program_2_date])

	if ''.join(workbook.cell(27,3).value.split(' ')).lower() == 'yes':
		incentive_program_3_cause = workbook.cell(27,4).value
		incentive_program_3_action = workbook.cell(27,5).value
		incentive_program_3_date = workbook.cell(27,6).value
		dynamic_variables.append([incentive_program_3_cause,incentive_program_3_action,incentive_program_3_date])

	if ''.join(workbook.cell(28,3).value.split(' ')).lower() == 'yes':
		violation_program_cause = workbook.cell(28,4).value
		violation_program_action = workbook.cell(28,5).value
		violation_program_date = workbook.cell(28,6).value
		dynamic_variables.append([violation_program_cause,violation_program_action,violation_program_date])

	if ''.join(workbook.cell(29,3).value.split(' ')).lower() == 'yes':
		sanction_program_1_cause = workbook.cell(29,4).value
		sanction_program_1_action = workbook.cell(29,5).value
		sanction_program_1_date = workbook.cell(29,6).value
		dynamic_variables.append([sanction_program_1_cause,sanction_program_1_action,sanction_program_1_date])

	if ''.join(workbook.cell(30,3).value.split(' ')).lower() == 'yes':
		sanction_program_2_cause = workbook.cell(30,4).value
		sanction_program_2_action = workbook.cell(30,5).value
		sanction_program_2_date = workbook.cell(30,6).value
		dynamic_variables.append([sanction_program_2_cause,sanction_program_2_action,sanction_program_2_date])

	if ''.join(workbook.cell(33,3).value.split(' ')).lower() != '':
		confinement_1_days = workbook.cell(33,4).value
		confinement_1_place = workbook.cell(33,5).value
		confinement_1_date = workbook.cell(33,6).value
		dynamic_variables.append([confinement_1_days,confinement_1_place,confinement_1_date])
	
	if ''.join(workbook.cell(34,3).value.split(' ')).lower() != '':
		confinement_2_days = workbook.cell(34,4).value
		confinement_2_place = workbook.cell(34,5).value
		confinement_2_date = workbook.cell(34,6).value
		dynamic_variables.append([confinement_2_days,confinement_2_place,confinement_2_date])

	if ''.join(workbook.cell(35,3).value.split(' ')).lower() != '':
		confinement_3_days = workbook.cell(35,4).value
		confinement_3_place = workbook.cell(35,5).value
		confinement_3_date = workbook.cell(35,6).value
		dynamic_variables.append([confinement_3_days,confinement_3_place,confinement_3_date])

	if ''.join(workbook.cell(37,3).value.split(' ')).lower() == 'yes':
		arrest_type = workbook.cell(37,4).value
		arrest_reason = workbook.cell(37,5).value
		arrest_date = workbook.cell(37,6).value
		dynamic_variables.append([arrest_type,arrest_reason,arrest_date])

	if ''.join(workbook.cell(38,3).value.split(' ')).lower() == 'yes':
		conviction_type = workbook.cell(38,4).value
		conviction_reason = workbook.cell(38,5).value
		conviction_date = workbook.cell(38,6).value
		dynamic_variables.append([conviction_type,conviction_reason,conviction_date])

	# Crear una variable historia-compendio para infracciones-etc.
	individual_program = locals()
	for old_key in dynamic_variables:
		individual_program[old_key+str(today_date)] = individual_program.pop(old_key)
	del individual_program['program_file'], individual_program['ID'], individual_program['workbook'], individual_program['dynamic_variables'], individual_program['today_date']
	# CHANGE NAMES - ADD 
	return pd.DataFrame(individual_program, index=[ID])

def update_parole(parole_file):
	parole_key = 1
	ID = 'DUMMY ID'
	date_updated_program_form = datetime.datetime(*xlrd.xldate_as_tuple(workbook.cell(5,2).value, xlrd.open_workbook(program_file).datemode)).date()
	individual_parole = locals()
	del individual_parole['parole_file'], individual_parole['ID']#individual_parole['workbook'], 
	return pd.DataFrame(individual_parole, index=[ID])

def consolidate_status(mother_db):
	"""
	# currently incarcerated - comes from demographics
	# removed pre-release from the program - comes from demographics 

	"""	
	try: 
		current_snapshot = mother_db.groupby('date_updated_program_form').agg(np.min)['status_program'].value_counts() + mother_db.groupby('date_updated_parole_form').agg(np.min)['status_program'].value_counts() # this should be added
	except KeyError:
		current_snapshot = mother_db.groupby('date_updated_program_form').agg(np.min)['status_program'].value_counts()

	current_snapshot.to_excel('current_snapshot_date.xls')

if __name__ == "__main__":

	path = './GR_IL_data'
	file_list = os.listdir(path)
	# Limitaciones: archivos repetidos, archivos vacios... no tan importante hasta que se generalice.

	# demographics.
	prerelease_db = pd.concat([update_prerelease(path+'/'+str(file)) for file in file_list if "pre-release" in file.lower()]) #WHAT HAPPENS IF IT'S EMPTY!
	program_db = pd.concat([update_program(path+'/'+str(file)) for file in file_list if "tasc" in file.lower()])
	#parole_db = pd.concat([update_parole(path+'/'+str(file)) for file in file_list if "Parole Measures" in file])

	mother_db = prerelease_db.merge(program_db, left_index=True, right_index=True, how='outer')
	mother_db.drop_duplicates().to_excel('GR_.xlsx')
	consolidate_status(mother_db)