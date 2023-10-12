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

###########################################################################
## Class PenaltyReporterMain
###########################################################################

class PenaltyReporterMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"NSW Penalty Reporter", pos = wx.DefaultPosition, size = wx.Size( 1200,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		MainPanel = wx.BoxSizer( wx.HORIZONTAL )

		MainVbox = wx.BoxSizer( wx.VERTICAL )

		self.Toolbar = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL )
		self.Toolbar.SetMargins( wx.Size( -2,-2 ) )
		self.m_filePicker1 = wx.FilePickerCtrl( self.Toolbar, wx.ID_ANY, u"G:\\My Drive\\Griffith\\Year 3\\Trimester 2\\2810ICT - Software Technologies\\Assignment\\archive\\penalty_data_set_2.csv", u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.Toolbar.AddControl( self.m_filePicker1 )
		self.Load = wx.Button( self.Toolbar, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Toolbar.AddControl( self.Load )
		self.Clear = wx.Button( self.Toolbar, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Toolbar.AddControl( self.Clear )
		self.Toolbar.Realize()

		MainVbox.Add( self.Toolbar, 0, wx.EXPAND, 5 )

		ProgramHBox = wx.BoxSizer( wx.HORIZONTAL )

		ToolPanel = wx.BoxSizer( wx.VERTICAL )

		TimeRange = wx.BoxSizer( wx.HORIZONTAL )

		self.FromText = wx.StaticText( self, wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FromText.Wrap( -1 )

		TimeRange.Add( self.FromText, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.FromDate = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		TimeRange.Add( self.FromDate, 0, wx.ALL, 5 )

		self.ToText = wx.StaticText( self, wx.ID_ANY, u"To:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ToText.Wrap( -1 )

		TimeRange.Add( self.ToText, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.ToDate = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		TimeRange.Add( self.ToDate, 0, wx.ALL, 5 )


		ToolPanel.Add( TimeRange, 0, wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		ToolPanel.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Data Options", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		ToolPanel.Add( self.m_staticText5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.ReportButton = wx.Button( self, wx.ID_ANY, u"Report", wx.DefaultPosition, wx.DefaultSize, 0 )
		ToolPanel.Add( self.ReportButton, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.ChartButton = wx.Button( self, wx.ID_ANY, u"Chart", wx.DefaultPosition, wx.DefaultSize, 0 )
		ToolPanel.Add( self.ChartButton, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_button21 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		ToolPanel.Add( self.m_button21, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button22 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		ToolPanel.Add( self.m_button22, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button23 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		ToolPanel.Add( self.m_button23, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		ProgramHBox.Add( ToolPanel, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		DisplayPanel = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		DisplayPanel.Add( self.m_panel1, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid1.CreateGrid( 5, 5 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )

		# Columns
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		DisplayPanel.Add( self.m_grid1, 3, wx.ALL|wx.EXPAND, 5 )


		ProgramHBox.Add( DisplayPanel, 1, wx.EXPAND, 5 )


		MainVbox.Add( ProgramHBox, 1, wx.EXPAND, 5 )


		MainPanel.Add( MainVbox, 1, wx.EXPAND, 5 )


		self.SetSizer( MainPanel )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


