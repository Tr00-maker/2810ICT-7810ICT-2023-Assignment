# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import wx.grid
import pandas as pd

###########################################################################
## Class PenaltyReporterMain
###########################################################################

class PenaltyReporterMain ( wx.Frame ):

	MAX_ROWS_PER_PAGE_OPTIONS = [50, 100, 200, 300]

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"NSW Penalty Reporter", pos = wx.DefaultPosition, size = wx.Size( 1200,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		MainPanel = wx.BoxSizer( wx.HORIZONTAL )

		MainVbox = wx.BoxSizer( wx.VERTICAL )

		self.Toolbar = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL )
		self.Toolbar.SetToolSeparation( 0 )
		self.Toolbar.SetMargins( wx.Size( -3,-3 ) )
		self.Toolbar.SetToolPacking( 15 )
		self.FilePicker = wx.FilePickerCtrl( self.Toolbar, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.Toolbar.AddControl( self.FilePicker )
		self.Load = wx.Button( self.Toolbar, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Load.Bind(wx.EVT_BUTTON, self.OnLoadButtonClick)
		self.Toolbar.AddControl( self.Load )
		self.Clear = wx.Button( self.Toolbar, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Toolbar.AddControl( self.Clear )
		self.Toolbar.Realize()

		MainVbox.Add( self.Toolbar, 0, wx.EXPAND, 5 )

		ProgramHBox = wx.BoxSizer( wx.HORIZONTAL )

		ToolPanel = wx.BoxSizer( wx.VERTICAL )

		self.Divider1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		ToolPanel.Add( self.Divider1, 0, wx.EXPAND |wx.ALL, 5 )

		self.DataHeading = wx.StaticText( self, wx.ID_ANY, u"Data Options", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DataHeading.Wrap( -1 )

		ToolPanel.Add( self.DataHeading, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		ReportPanel = wx.BoxSizer( wx.VERTICAL )

		self.ReportHeading = wx.StaticText( self, wx.ID_ANY, u"Report", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ReportHeading.Wrap( -1 )

		self.ReportHeading.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )

		ReportPanel.Add( self.ReportHeading, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		TimeRange1 = wx.BoxSizer( wx.HORIZONTAL )

		self.FromText1 = wx.StaticText( self, wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FromText1.Wrap( -1 )

		TimeRange1.Add( self.FromText1, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.FromDate1 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT|wx.adv.DP_DROPDOWN )
		TimeRange1.Add( self.FromDate1, 0, wx.ALL, 5 )

		self.ToText1 = wx.StaticText( self, wx.ID_ANY, u"To:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ToText1.Wrap( -1 )

		TimeRange1.Add( self.ToText1, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.ToDate1 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT|wx.adv.DP_DROPDOWN )
		TimeRange1.Add( self.ToDate1, 0, wx.ALL, 5 )


		ReportPanel.Add( TimeRange1, 0, 0, 5 )

		self.ReportButton = wx.Button( self, wx.ID_ANY, u"Report", wx.DefaultPosition, wx.DefaultSize, 0 )
		ReportPanel.Add( self.ReportButton, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Filter by Offence", wx.DefaultPosition, wx.DefaultSize, 0 )
		ReportPanel.Add( self.m_checkBox1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		m_comboBox1Choices = []
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		ReportPanel.Add( self.m_comboBox1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		ToolPanel.Add( ReportPanel, 1, wx.EXPAND, 5 )

		self.Divider2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		ToolPanel.Add( self.Divider2, 0, wx.EXPAND |wx.ALL, 5 )

		ChartPanel = wx.BoxSizer( wx.VERTICAL )

		self.ChartHeading = wx.StaticText( self, wx.ID_ANY, u"Chart", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ChartHeading.Wrap( -1 )

		self.ChartHeading.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )

		ChartPanel.Add( self.ChartHeading, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		TimeRange2 = wx.BoxSizer( wx.HORIZONTAL )

		self.FromText2 = wx.StaticText( self, wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FromText2.Wrap( -1 )

		TimeRange2.Add( self.FromText2, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.FromDate2 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT|wx.adv.DP_DROPDOWN )
		TimeRange2.Add( self.FromDate2, 0, wx.ALL, 5 )

		self.ToText2 = wx.StaticText( self, wx.ID_ANY, u"To:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ToText2.Wrap( -1 )

		TimeRange2.Add( self.ToText2, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.ToDate2 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT|wx.adv.DP_DROPDOWN )
		TimeRange2.Add( self.ToDate2, 0, wx.ALL, 5 )


		ChartPanel.Add( TimeRange2, 0, 0, 5 )

		self.ChartButton = wx.Button( self, wx.ID_ANY, u"Chart", wx.DefaultPosition, wx.DefaultSize, 0 )
		ChartPanel.Add( self.ChartButton, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_checkBox11 = wx.CheckBox( self, wx.ID_ANY, u"Filter by Offence", wx.DefaultPosition, wx.DefaultSize, 0 )
		ChartPanel.Add( self.m_checkBox11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		m_comboBox11Choices = []
		self.m_comboBox11 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBox11Choices, 0 )
		ChartPanel.Add( self.m_comboBox11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		ToolPanel.Add( ChartPanel, 1, wx.EXPAND, 5 )

		self.Divider3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		ToolPanel.Add( self.Divider3, 0, wx.EXPAND |wx.ALL, 5 )


		ToolPanel.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		ProgramHBox.Add( ToolPanel, 0, wx.EXPAND, 5 )

		DisplayPanel = wx.BoxSizer( wx.VERTICAL )

		self.ChartPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
		self.ChartPanel.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		DisplayPanel.Add( self.ChartPanel, 2, wx.ALL|wx.EXPAND, 5 )

		#create grid but dont yet populate
		self.Grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		data = [] #data attribute

		# Grid
		self.Grid.CreateGrid( 5, 5 )
		self.Grid.EnableEditing( True )
		self.Grid.EnableGridLines( True )
		self.Grid.EnableDragGridSize( False )
		self.Grid.SetMargins( 0, 0 )

		# Columns
		self.Grid.EnableDragColMove( False )
		self.Grid.EnableDragColSize( True )
		self.Grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.Grid.EnableDragRowSize( True )
		self.Grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.Grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		DisplayPanel.Add( self.Grid, 3, wx.ALL|wx.EXPAND, 5 )


		ProgramHBox.Add( DisplayPanel, 1, wx.EXPAND, 5 )


		MainVbox.Add( ProgramHBox, 1, wx.EXPAND, 5 )


		MainPanel.Add( MainVbox, 1, wx.EXPAND, 5 )


		self.SetSizer( MainPanel )
		self.Layout()

		self.Centre( wx.BOTH )

		#program variables
		
		self.current_max_rows_per_page = self.MAX_ROWS_PER_PAGE_OPTIONS[0]

	def __del__( self ):
		pass

	def OnLoadButtonClick(self, event):

		#get selected file path
		file_path = self.FilePicker.GetPath()

		#load data from the CSV
		data = self.load_data_from_csv(file_path)

		#set page and rows per page
		page = 0
		max_rows_per_page = self.current_max_rows_per_page

		#populate
		self.populate_grid(data, page, max_rows_per_page)

	def OnClearButtonClick(self, event):
		#clear grid
		self.Grid.ClearGrid()

	def load_data_from_csv(self, file_path):
		try:
			#read csv file using Pandas
			data = pd.read_csv(file_path)

			#convert pandas DataFrame to list of lists
			data_as_list = data.values.tolist()

			return data_as_list
		except Exception as e:
			#handle any potential exceptions, eg, file not found
			print(f"Error loading data: {str(e)}")
			return []

	def populate_grid(self, data, page, max_rows_per_page):
		
		#clear grid
		self.Grid.ClearGrid()
		num_rows = len(data)
		print(num_rows)

		#set the number of rows/columns based on the data
		start_row = page * max_rows_per_page
		end_row = min((page + 1) * max_rows_per_page, len(data))
		num_cols = len(data[0]) if start_row < len(data) else 0

		#update column labels
		for col in range(num_cols):
			column_label = data[0][col] #first row contains column names
			self.Grid.SetColLabelValue(col, str(column_label))
		
		print("num_rows:", num_rows)
		print("start_row:", start_row)
		print("end_row:", end_row)

		#check if grid size needs adjusting
		if end_row > self.Grid.GetNumberRows():
			self.Grid.AppendRows(end_row - self.Grid.GetNumberRows())
		if num_cols > self.Grid.GetNumberCols():
			self.Grid.AppendCols(num_cols - self.Grid.GetNumberCols())
		print("num_cols:", num_cols)

		

		#populate
		for row in range(start_row, end_row):
			for col in range(num_cols):
				value = data[row][col]
				#check if indices are valid
				if row < self.Grid.GetNumberRows() and col < self.Grid.GetNumberCols():
					self.Grid.SetCellValue(row - start_row, col, str(value))

if __name__ == '__main__':
    app = wx.App()
    # Check if the frame is already shown, if not, create and show
    top_window = wx.GetApp().GetTopWindow()
    if not top_window:
        frame = PenaltyReporterMain(None)
        frame.Show()
    app.MainLoop()


