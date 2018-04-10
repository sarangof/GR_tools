import numpy as np
#from bokeh.plotting import figure, output_file, show
import pandas as pd   
from bokeh.io import show, output_file, curdoc
from bokeh.models import ColumnDataSource, TableColumn, DataTable
from bokeh.layouts import row, widgetbox, column, gridplot
from bokeh.resources import CDN
from bokeh.plotting import figure, output_file
from bokeh.transform import factor_cmap

output_file('GR_viz.html')

def demographics():
	pass

def status():
	'prerelease_key','program_key'
	pass

def prerelease_programming(db):

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

def prerelease_preparation(db):
	#output_file("colormapped_bars.html")
	def number_yes(db,column):
		try:
			return sum(int(''.join(x.lower().split(' '))=='yes') for x in db[column]) # WHAT HAPPENS IF NO IS THE LARGEST VALUE. DUH.
		except IndexError:
			return 0

	completion_columns = ['ID_completion', 'SS_card', 'birth_certificate', 'release_plan','resume']
	counts = [number_yes(db,column) for column in completion_columns]
	#print(counts)

	source = ColumnDataSource(data=dict(documents=completion_columns, counts=counts))

	p = figure(x_range=completion_columns, plot_height=250, title="Pre-release preparation")
	p.vbar(x='documents', top='counts', width=0.9, source=source, legend=None, line_color='white')

	# SAVE AS PNG
	return p

def postrelease_incentives():
	pass

def postrelease_violations():
	pass

def postrelease_sanctions():
	pass
def postrelease_arrests():
	pass

def postrelease_convictions():
	pass

def postrelease_revocations():
	pass

def post_release_treatment():
	pass


db = pd.read_excel('GR_.xlsx')
barplot_prerelease_preparation = prerelease_preparation(db)
barplot_prerelease_preparation.xgrid.grid_line_color = None
table_prerelease_programming = prerelease_programming(db)

p = gridplot([[barplot_prerelease_preparation, table_prerelease_programming]], toolbar_location='left')

show(p)
#show(barplot_prerelease_preparation)
#curdoc().title = "Dashboard"
#curdoc().add_root(column(barplot_prerelease_preparation,table_prerelease_programming))



#p.xgrid.grid_line_color = None
#p.y_range.start = 0
#p.y_range.end = 9
#p.legend.orientation = "horizontal"
#p.legend.location = "top_center"







