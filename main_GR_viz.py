import numpy as np
#from bokeh.plotting import figure, output_file, show
import pandas as pd   
from bokeh.io import show, output_file, curdoc
from bokeh.models import ColumnDataSource, TableColumn, DataTable, Dropdown
from bokeh.layouts import row, widgetbox, column, gridplot
from bokeh.resources import CDN
from bokeh.plotting import figure, output_file
from bokeh.transform import factor_cmap

#output_file('GR_viz.html')

def demographics():
	return None

def status(db):

	# currently incarcerated
	# removed pre-release from the program 
	# currently on electronic detention in the community
	# currently on MSR--# with/without electronic monitoring
	# currently post-MSR

	#if db[['prerelease_key','program_key']].sum(axis=1) >= 2:
	#	pass
	#elif db['prerelease_key'] == 1:
	#	pass

	return None

def programming(db):
	source = ColumnDataSource(ColumnDataSource.from_df(db.reset_index()))
	#source.add(db.index, 'index')
	
	columns = [
		TableColumn(field="ID", title="ID"),
	    TableColumn(field="TFC_complete", title="T4C complete"),
	    TableColumn(field="TFC_sessions", title="T4C sessions"),
	    TableColumn(field="partial_college_prerelase_total", title="College programming"),
	    TableColumn(field="GED_prerelease", title="GED"),
	    TableColumn(field="certificate_programs_prerelease", title="Certificate programs")
	]
	
	data_table = DataTable(source=source, columns=columns, width=800)
	data_table.index_position = None
	table = widgetbox(data_table)
	#curdoc().add_root(row(controls, table))
	#curdoc().title = "Export CSV"
	return table

def basic_needs(db):
	def number_yes(db,column):
		try:
			return sum(int(''.join(x.lower().split(' '))=='yes') for x in db[column]) 
		except IndexError:
			return 0

	completion_columns = ['ID_completion', 'SS_card', 'birth_certificate', 'release_plan','resume']
	counts = [number_yes(db,column) for column in completion_columns]
	#print(counts)
	source = ColumnDataSource(data=dict(documents=completion_columns, counts=counts))

	p = figure(x_range=completion_columns, plot_height=250, title="Pre-release preparation")
	p.vbar(x='documents', top='counts', width=0.9, source=source, legend=None, line_color='white')

	return p

def violations_sanctions(db):
	return None

def employment_community(db):
	return None

def Family(db):
	return None

def Fidelity(db):
	return None

def Individual(db):
	return None

db = pd.read_excel('GR_.xlsx')

#p = gridplot([[barplot_prerelease_preparation, table_prerelease_programming]], toolbar_location='left')

category_names = { 
	'Demographics':'demographics',
	'Status': 'status',		
	'Programming':'programming',
	'Basic needs':'basic_needs',
	'Rewards/Sanctions/Violations':'violations_sanctions',
	'Employment and community':'employment_community',
	'Family':'Family',
	'Fidelity':'Fidelity',
	'Individual':'Individual'
}


def update_dropdown(db, category_names = []):
	if not category_names:
		plot = None
	else:
		print("Here I am.")
		plot = globals()[category_names[str(dropdown.value)]](db)
	return plot

print("HOLI")

dropdown = Dropdown(label = 'Categories', menu = [(x,y) for x,y in zip(category_names.keys(), category_names.keys())], value='Basic needs')
dropdown.on_change('value', lambda attr, old, new: update_dropdown(db,category_names))#, lambda attr, old, new: update_view())

dropdown_widget = widgetbox(dropdown)

plot=basic_needs(db)
curdoc().add_root(row(dropdown_widget,plot))
curdoc().title = "Dashboard"

update_dropdown(db)

#show(barplot_prerelease_preparation)
#curdoc().title = "Dashboard"
#curdoc().add_root(column(barplot_prerelease_preparation,table_prerelease_programming))

#p.xgrid.grid_line_color = None
#p.y_range.start = 0
#p.y_range.end = 9
#p.legend.orientation = "horizontal"
#p.legend.location = "top_center"