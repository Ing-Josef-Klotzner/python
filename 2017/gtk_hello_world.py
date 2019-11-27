#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals, print_function
"""
Created on Tue Jul 25 19:43:24 2017

@author: josef
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.button1 = Gtk.Button(label="Hello")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 3)

        self.button2 = Gtk.Button(label="Goodbye")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 3)

    def on_button1_clicked(self, widget):
        print("Hello")

    def on_button2_clicked(self, widget):
        print("Goodbye")

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

"""
>>> dir (Gtk.Button().props)
['action_name', 'action_target', 'always_show_image', 'app_paintable', 'border_width',\
 'can_default', 'can_focus', 'child', 'composite_child', 'double_buffered', 'events', 'expand',\
 'focus_on_click', 'halign', 'has_default', 'has_focus', 'has_tooltip', 'height_request',\
 'hexpand', 'hexpand_set', 'image', 'image_position', 'is_focus', 'label', 'margin',\
 'margin_bottom', 'margin_left', 'margin_right', 'margin_top', 'name', 'no_show_all', \
 'opacity', 'parent', 'receives_default', 'related_action', 'relief', 'resize_mode',\
 'scale_factor', 'sensitive', 'style', 'tooltip_markup', 'tooltip_text',\
 'use_action_appearance', 'use_stock', 'use_underline', 'valign', 'vexpand', 'vexpand_set',\
 'visible', 'width_request', 'window', 'xalign', 'yalign']
 
>>> dir(Gtk.Box().props)
['app_paintable', 'baseline_position', 'border_width', 'can_default', 'can_focus', 'child',\
 'composite_child', 'double_buffered', 'events', 'expand', 'halign', 'has_default', 'has_focus',\
 'has_tooltip', 'height_request', 'hexpand', 'hexpand_set', 'homogeneous', 'is_focus', 'margin',\
 'margin_bottom', 'margin_left', 'margin_right', 'margin_top', 'name', 'no_show_all', 'opacity',\
 'orientation', 'parent', 'receives_default', 'resize_mode', 'scale_factor', 'sensitive', \
 'spacing', 'style', 'tooltip_markup', 'tooltip_text', 'valign', 'vexpand', 'vexpand_set',\
 'visible', 'width_request', 'window']

>>> dir(Gtk)
['AboutDialog', 'AboutDialogClass', 'AboutDialogPrivate', 'AccelFlags', 'AccelGroup',\
 'AccelGroupClass', 'AccelGroupEntry', 'AccelGroupPrivate', 'AccelKey', 'AccelLabel',\
 'AccelLabelClass', 'AccelLabelPrivate', 'AccelMap', 'AccelMapClass', 'Accessible', \
 'AccessibleClass', 'AccessiblePrivate', 'Action', 'ActionClass', 'ActionEntry', \
 'ActionGroup', 'ActionGroupClass', 'ActionGroupPrivate', 'ActionPrivate', 'Actionable',\
 'ActionableInterface', 'Activatable', 'ActivatableIface', 'Adjustment', 'AdjustmentClass',\
 'AdjustmentPrivate', 'Align', 'Alignment', 'AlignmentClass', 'AlignmentPrivate', 'AppChooser',\
 'AppChooserButton', 'AppChooserButtonClass', 'AppChooserButtonPrivate', 'AppChooserDialog',\
 'AppChooserDialogClass', 'AppChooserDialogPrivate', 'AppChooserWidget', 'AppChooserWidgetClass',\
 'AppChooserWidgetPrivate', 'Application', 'ApplicationClass', 'ApplicationInhibitFlags',\
 'ApplicationPrivate', 'ApplicationWindow', 'ApplicationWindowClass', 'ApplicationWindowPrivate',\
 'Arrow', 'ArrowClass', 'ArrowPlacement', 'ArrowPrivate', 'ArrowType', 'AspectFrame',\
 'AspectFrameClass', 'AspectFramePrivate', 'Assistant', 'AssistantClass', 'AssistantPageType',\
 'AssistantPrivate', 'AttachOptions', 'BINARY_AGE', 'BaselinePosition', 'Bin', 'BinClass',\
 'BinPrivate', 'BindingArg', 'BindingEntry', 'BindingSet', 'BindingSignal', 'Border', \
 'BorderStyle', 'Box', 'BoxClass', 'BoxPrivate', 'Buildable', 'BuildableIface', 'Builder',\
 'BuilderClass', 'BuilderError', 'BuilderPrivate', 'Button', 'ButtonBox', 'ButtonBoxClass',\
 'ButtonBoxPrivate', 'ButtonBoxStyle', 'ButtonClass', 'ButtonPrivate', 'ButtonsType', 'Calendar',\
 'CalendarClass', 'CalendarDisplayOptions', 'CalendarPrivate', 'CellArea', 'CellAreaBox',\
 'CellAreaBoxClass', 'CellAreaBoxPrivate', 'CellAreaClass', 'CellAreaContext',\
 'CellAreaContextClass', 'CellAreaContextPrivate', 'CellAreaPrivate', 'CellEditable', \
 'CellEditableIface', 'CellLayout', 'CellLayoutIface', 'CellRenderer', 'CellRendererAccel',\
 'CellRendererAccelClass', 'CellRendererAccelMode', 'CellRendererAccelPrivate',\
 'CellRendererClass', 'CellRendererClassPrivate', 'CellRendererCombo', 'CellRendererComboClass',\
 'CellRendererComboPrivate', 'CellRendererMode', 'CellRendererPixbuf', 'CellRendererPixbufClass',\
 'CellRendererPixbufPrivate', 'CellRendererPrivate', 'CellRendererProgress',\
 'CellRendererProgressClass', 'CellRendererProgressPrivate', 'CellRendererSpin',\
 'CellRendererSpinClass', 'CellRendererSpinPrivate', 'CellRendererSpinner',\
 'CellRendererSpinnerClass', 'CellRendererSpinnerPrivate', 'CellRendererState',\
 'CellRendererText', 'CellRendererTextClass', 'CellRendererTextPrivate', 'CellRendererToggle',\
 'CellRendererToggleClass', 'CellRendererTogglePrivate', 'CellView', 'CellViewClass',\
 'CellViewPrivate', 'CheckButton', 'CheckButtonClass', 'CheckMenuItem', 'CheckMenuItemClass',\
 'CheckMenuItemPrivate', 'Clipboard', 'ColorButton', 'ColorButtonClass', 'ColorButtonPrivate',\
 'ColorChooser', 'ColorChooserDialog', 'ColorChooserDialogClass', 'ColorChooserDialogPrivate',\
 'ColorChooserInterface', 'ColorChooserWidget', 'ColorChooserWidgetClass',\
 'ColorChooserWidgetPrivate', 'ColorSelection', 'ColorSelectionClass', 'ColorSelectionDialog',\
 'ColorSelectionDialogClass', 'ColorSelectionDialogPrivate', 'ColorSelectionPrivate', 'ComboBox',\
 'ComboBoxClass', 'ComboBoxPrivate', 'ComboBoxText', 'ComboBoxTextClass', 'ComboBoxTextPrivate',\
 'Container', 'ContainerClass', 'ContainerPrivate', 'CornerType', 'CssProvider',\
 'CssProviderClass', 'CssProviderError', 'CssProviderPrivate', 'CssSection', 'CssSectionType',\
 'DebugFlag', 'DeleteType', 'DestDefaults', 'Dialog', 'DialogClass', 'DialogFlags',\
 'DialogPrivate', 'DirectionType', 'DragResult', 'DrawingArea', 'DrawingAreaClass', 'Editable',\
 'EditableInterface', 'Entry', 'EntryBuffer', 'EntryBufferClass', 'EntryBufferPrivate',\
 'EntryClass', 'EntryCompletion', 'EntryCompletionClass', 'EntryCompletionPrivate',\
 'EntryIconPosition', 'EntryPrivate', 'EventBox', 'EventBoxClass', 'EventBoxPrivate',\
 'Expander', 'ExpanderClass', 'ExpanderPrivate', 'ExpanderStyle', 'FileChooser', \
 'FileChooserAction', 'FileChooserButton', 'FileChooserButtonClass', 'FileChooserButtonPrivate',\
 'FileChooserConfirmation', 'FileChooserDialog', 'FileChooserDialogClass',\
 'FileChooserDialogPrivate', 'FileChooserError', 'FileChooserWidget', 'FileChooserWidgetClass',\
 'FileChooserWidgetPrivate', 'FileFilter', 'FileFilterFlags', 'FileFilterInfo', 'Fixed',\
 'FixedChild', 'FixedClass', 'FixedPrivate', 'FontButton', 'FontButtonClass', 'FontButtonPrivate',\
 'FontChooser', 'FontChooserDialog', 'FontChooserDialogClass', 'FontChooserDialogPrivate',\
 'FontChooserIface', 'FontChooserWidget', 'FontChooserWidgetClass', 'FontChooserWidgetPrivate',\
 'FontSelection', 'FontSelectionClass', 'FontSelectionDialog', 'FontSelectionDialogClass',\
 'FontSelectionDialogPrivate', 'FontSelectionPrivate', 'Frame', 'FrameClass', 'FramePrivate',\
 'Gradient', 'Grid', 'GridClass', 'GridPrivate', 'HBox', 'HBoxClass', 'HButtonBox',\
 'HButtonBoxClass', 'HPaned', 'HPanedClass', 'HSV', 'HSVClass', 'HSVPrivate', 'HScale',\
 'HScaleClass', 'HScrollbar', 'HScrollbarClass', 'HSeparator', 'HSeparatorClass', 'HandleBox',\
 'HandleBoxClass', 'HandleBoxPrivate', 'HeaderBar', 'HeaderBarClass', 'HeaderBarPrivate',\
 'IMContext', 'IMContextClass', 'IMContextInfo', 'IMContextSimple', 'IMContextSimpleClass',\
 'IMContextSimplePrivate', 'IMMulticontext', 'IMMulticontextClass', 'IMMulticontextPrivate',\
 'IMPreeditStyle', 'IMStatusStyle', 'INPUT_ERROR', 'INTERFACE_AGE', 'IconFactory',\
 'IconFactoryClass', 'IconFactoryPrivate', 'IconInfo', 'IconInfoClass', 'IconLookupFlags',\
 'IconSet', 'IconSize', 'IconSource', 'IconTheme', 'IconThemeClass', 'IconThemeError',\
 'IconThemePrivate', 'IconView', 'IconViewClass', 'IconViewDropPosition', 'IconViewPrivate',\
 'Image', 'ImageClass', 'ImageMenuItem', 'ImageMenuItemClass', 'ImageMenuItemPrivate',\
 'ImagePrivate', 'ImageType', 'InfoBar', 'InfoBarClass', 'InfoBarPrivate', 'InputHints',\
 'InputPurpose', 'Invisible', 'InvisibleClass', 'InvisiblePrivate', 'JunctionSides',\
 'Justification', 'LEVEL_BAR_OFFSET_HIGH', 'LEVEL_BAR_OFFSET_LOW', 'Label', 'LabelClass',\
 'LabelPrivate', 'LabelSelectionInfo', 'Layout', 'LayoutClass', 'LayoutPrivate', 'LevelBar',\
 'LevelBarClass', 'LevelBarMode', 'LevelBarPrivate', 'License', 'LinkButton', 'LinkButtonClass',\
 'LinkButtonPrivate', 'ListBox', 'ListBoxClass', 'ListBoxRow', 'ListBoxRowClass', 'ListStore',\
 'ListStoreClass', 'ListStorePrivate', 'LockButton', 'LockButtonClass', 'LockButtonPrivate',\
 'MAJOR_VERSION', 'MAX_COMPOSE_LEN', 'MICRO_VERSION', 'MINOR_VERSION', 'Menu', 'MenuBar',\
 'MenuBarClass', 'MenuBarPrivate', 'MenuButton', 'MenuButtonClass', 'MenuButtonPrivate',\
 'MenuClass', 'MenuDirectionType', 'MenuItem', 'MenuItemClass', 'MenuItemPrivate', 'MenuPrivate',\
 'MenuShell', 'MenuShellClass', 'MenuShellPrivate', 'MenuToolButton', 'MenuToolButtonClass',\
 'MenuToolButtonPrivate', 'MessageDialog', 'MessageDialogClass', 'MessageDialogPrivate',\
 'MessageType', 'Misc', 'MiscClass', 'MiscPrivate', 'MountOperation', 'MountOperationClass',\
 'MountOperationPrivate', 'MovementStep', 'Notebook', 'NotebookClass', 'NotebookPrivate',\
 'NotebookTab', 'NumberUpLayout', 'NumerableIcon', 'NumerableIconClass', 'NumerableIconPrivate',\
 'OffscreenWindow', 'OffscreenWindowClass', 'Orientable', 'OrientableIface', 'Orientation',\
 'Overlay', 'OverlayClass', 'OverlayPrivate', 'PAPER_NAME_A3', 'PAPER_NAME_A4', 'PAPER_NAME_A5',\
 'PAPER_NAME_B5', 'PAPER_NAME_EXECUTIVE', 'PAPER_NAME_LEGAL', 'PAPER_NAME_LETTER',\
 'PATH_PRIO_MASK', 'PRINT_SETTINGS_COLLATE', 'PRINT_SETTINGS_DEFAULT_SOURCE',\
 'PRINT_SETTINGS_DITHER', 'PRINT_SETTINGS_DUPLEX', 'PRINT_SETTINGS_FINISHINGS',\
 'PRINT_SETTINGS_MEDIA_TYPE', 'PRINT_SETTINGS_NUMBER_UP', 'PRINT_SETTINGS_NUMBER_UP_LAYOUT',\
 'PRINT_SETTINGS_N_COPIES', 'PRINT_SETTINGS_ORIENTATION', 'PRINT_SETTINGS_OUTPUT_BASENAME',\
 'PRINT_SETTINGS_OUTPUT_BIN', 'PRINT_SETTINGS_OUTPUT_DIR', 'PRINT_SETTINGS_OUTPUT_FILE_FORMAT',\
 'PRINT_SETTINGS_OUTPUT_URI', 'PRINT_SETTINGS_PAGE_RANGES', 'PRINT_SETTINGS_PAGE_SET',\
 'PRINT_SETTINGS_PAPER_FORMAT', 'PRINT_SETTINGS_PAPER_HEIGHT', 'PRINT_SETTINGS_PAPER_WIDTH',\
 'PRINT_SETTINGS_PRINTER', 'PRINT_SETTINGS_PRINTER_LPI', 'PRINT_SETTINGS_PRINT_PAGES',\
 'PRINT_SETTINGS_QUALITY', 'PRINT_SETTINGS_RESOLUTION', 'PRINT_SETTINGS_RESOLUTION_X', \
 'PRINT_SETTINGS_RESOLUTION_Y', 'PRINT_SETTINGS_REVERSE', 'PRINT_SETTINGS_SCALE', \
 'PRINT_SETTINGS_USE_COLOR', 'PRINT_SETTINGS_WIN32_DRIVER_EXTRA',\
 'PRINT_SETTINGS_WIN32_DRIVER_VERSION', 'PRIORITY_RESIZE', 'PackDirection', 'PackType',\
 'PageOrientation', 'PageRange', 'PageSet', 'PageSetup', 'Paned', 'PanedClass', 'PanedPrivate',\
 'PaperSize', 'PathPriorityType', 'PathType', 'PlacesOpenFlags', 'PlacesSidebar',\
 'PlacesSidebarClass', 'Plug', 'PlugClass', 'PlugPrivate', 'PolicyType', 'PositionType', \
 'PrintContext', 'PrintDuplex', 'PrintError', 'PrintOperation', 'PrintOperationAction',\
 'PrintOperationClass', 'PrintOperationPreview', 'PrintOperationPreviewIface', \
 'PrintOperationPrivate', 'PrintOperationResult', 'PrintPages', 'PrintQuality', 'PrintSettings',\
 'PrintStatus', 'ProgressBar', 'ProgressBarClass', 'ProgressBarPrivate',\
 'PyGTKDeprecationWarning', 'RadioAction', 'RadioActionClass', 'RadioActionEntry',\
 'RadioActionPrivate', 'RadioButton', 'RadioButtonClass', 'RadioButtonPrivate',\
 'RadioMenuItem', 'RadioMenuItemClass', 'RadioMenuItemPrivate', 'RadioToolButton',\
 'RadioToolButtonClass', 'Range', 'RangeClass', 'RangePrivate', 'RcContext', 'RcFlags',\
 'RcProperty', 'RcStyle', 'RcStyleClass', 'RcTokenType', 'RecentAction', 'RecentActionClass',\
 'RecentActionPrivate', 'RecentChooser', 'RecentChooserDialog', 'RecentChooserDialogClass',\
 'RecentChooserDialogPrivate', 'RecentChooserError', 'RecentChooserIface', 'RecentChooserMenu',\
 'RecentChooserMenuClass', 'RecentChooserMenuPrivate', 'RecentChooserWidget',\
 'RecentChooserWidgetClass', 'RecentChooserWidgetPrivate', 'RecentData', 'RecentFilter',\
 'RecentFilterFlags', 'RecentFilterInfo', 'RecentInfo', 'RecentManager', 'RecentManagerClass',\
 'RecentManagerError', 'RecentManagerPrivate', 'RecentSortType', 'RegionFlags', 'ReliefStyle',\
 'RequestedSize', 'Requisition', 'ResizeMode', 'ResponseType', 'Revealer', 'RevealerClass',\
 'RevealerTransitionType', 'STOCK_ABOUT', 'STOCK_ADD', 'STOCK_APPLY', 'STOCK_BOLD',\
 'STOCK_CANCEL', 'STOCK_CAPS_LOCK_WARNING', 'STOCK_CDROM', 'STOCK_CLEAR', 'STOCK_CLOSE',\
 'STOCK_COLOR_PICKER', 'STOCK_CONNECT', 'STOCK_CONVERT', 'STOCK_COPY', 'STOCK_CUT',\
 'STOCK_DELETE', 'STOCK_DIALOG_AUTHENTICATION', 'STOCK_DIALOG_ERROR', 'STOCK_DIALOG_INFO',\
 'STOCK_DIALOG_QUESTION', 'STOCK_DIALOG_WARNING', 'STOCK_DIRECTORY', 'STOCK_DISCARD',\
 'STOCK_DISCONNECT', 'STOCK_DND', 'STOCK_DND_MULTIPLE', 'STOCK_EDIT', 'STOCK_EXECUTE', \
 'STOCK_FILE', 'STOCK_FIND', 'STOCK_FIND_AND_REPLACE', 'STOCK_FLOPPY', 'STOCK_FULLSCREEN',\
 'STOCK_GOTO_BOTTOM', 'STOCK_GOTO_FIRST', 'STOCK_GOTO_LAST', 'STOCK_GOTO_TOP', 'STOCK_GO_BACK',\
 'STOCK_GO_DOWN', 'STOCK_GO_FORWARD', 'STOCK_GO_UP', 'STOCK_HARDDISK', 'STOCK_HELP',\
 'STOCK_HOME', 'STOCK_INDENT', 'STOCK_INDEX', 'STOCK_INFO', 'STOCK_ITALIC', 'STOCK_JUMP_TO',\
 'STOCK_JUSTIFY_CENTER', 'STOCK_JUSTIFY_FILL', 'STOCK_JUSTIFY_LEFT', 'STOCK_JUSTIFY_RIGHT',\
 'STOCK_LEAVE_FULLSCREEN', 'STOCK_MEDIA_FORWARD', 'STOCK_MEDIA_NEXT', 'STOCK_MEDIA_PAUSE',\
 'STOCK_MEDIA_PLAY', 'STOCK_MEDIA_PREVIOUS', 'STOCK_MEDIA_RECORD', 'STOCK_MEDIA_REWIND',\
 'STOCK_MEDIA_STOP', 'STOCK_MISSING_IMAGE', 'STOCK_NETWORK', 'STOCK_NEW', 'STOCK_NO',\
 'STOCK_OK', 'STOCK_OPEN', 'STOCK_ORIENTATION_LANDSCAPE', 'STOCK_ORIENTATION_PORTRAIT',\
 'STOCK_ORIENTATION_REVERSE_LANDSCAPE', 'STOCK_ORIENTATION_REVERSE_PORTRAIT',\
 'STOCK_PAGE_SETUP', 'STOCK_PASTE', 'STOCK_PREFERENCES', 'STOCK_PRINT', 'STOCK_PRINT_ERROR',\
 'STOCK_PRINT_PAUSED', 'STOCK_PRINT_PREVIEW', 'STOCK_PRINT_REPORT', 'STOCK_PRINT_WARNING',\
 'STOCK_PROPERTIES', 'STOCK_QUIT', 'STOCK_REDO', 'STOCK_REFRESH', 'STOCK_REMOVE',\
 'STOCK_REVERT_TO_SAVED', 'STOCK_SAVE', 'STOCK_SAVE_AS', 'STOCK_SELECT_ALL',\
 'STOCK_SELECT_COLOR', 'STOCK_SELECT_FONT', 'STOCK_SORT_ASCENDING', 'STOCK_SORT_DESCENDING',\
 'STOCK_SPELL_CHECK', 'STOCK_STOP', 'STOCK_STRIKETHROUGH', 'STOCK_UNDELETE', 'STOCK_UNDERLINE',\
 'STOCK_UNDO', 'STOCK_UNINDENT', 'STOCK_YES', 'STOCK_ZOOM_100', 'STOCK_ZOOM_FIT',\
 'STOCK_ZOOM_IN', 'STOCK_ZOOM_OUT', 'STYLE_CLASS_ACCELERATOR', 'STYLE_CLASS_ARROW',\
 'STYLE_CLASS_BACKGROUND', 'STYLE_CLASS_BOTTOM', 'STYLE_CLASS_BUTTON', 'STYLE_CLASS_CALENDAR',\
 'STYLE_CLASS_CELL', 'STYLE_CLASS_CHECK', 'STYLE_CLASS_COMBOBOX_ENTRY',\
 'STYLE_CLASS_CONTEXT_MENU', 'STYLE_CLASS_CURSOR_HANDLE', 'STYLE_CLASS_DEFAULT',\
 'STYLE_CLASS_DIM_LABEL', 'STYLE_CLASS_DND', 'STYLE_CLASS_DOCK', 'STYLE_CLASS_ENTRY', \
 'STYLE_CLASS_ERROR', 'STYLE_CLASS_EXPANDER', 'STYLE_CLASS_FRAME', 'STYLE_CLASS_GRIP',\
 'STYLE_CLASS_HEADER', 'STYLE_CLASS_HIGHLIGHT', 'STYLE_CLASS_HORIZONTAL', 'STYLE_CLASS_IMAGE',\
 'STYLE_CLASS_INFO', 'STYLE_CLASS_INLINE_TOOLBAR', 'STYLE_CLASS_INSERTION_CURSOR',\
 'STYLE_CLASS_LEFT', 'STYLE_CLASS_LEVEL_BAR', 'STYLE_CLASS_LINKED', 'STYLE_CLASS_LIST', \
 'STYLE_CLASS_LIST_ROW', 'STYLE_CLASS_MARK', 'STYLE_CLASS_MENU', 'STYLE_CLASS_MENUBAR',\
 'STYLE_CLASS_MENUITEM', 'STYLE_CLASS_NOTEBOOK', 'STYLE_CLASS_OSD', \
 'STYLE_CLASS_PANE_SEPARATOR', 'STYLE_CLASS_PRIMARY_TOOLBAR', 'STYLE_CLASS_PROGRESSBAR',\
 'STYLE_CLASS_PULSE', 'STYLE_CLASS_QUESTION', 'STYLE_CLASS_RADIO', 'STYLE_CLASS_RAISED',\
 'STYLE_CLASS_READ_ONLY', 'STYLE_CLASS_RIGHT', 'STYLE_CLASS_RUBBERBAND', 'STYLE_CLASS_SCALE',\
 'STYLE_CLASS_SCALE_HAS_MARKS_ABOVE', 'STYLE_CLASS_SCALE_HAS_MARKS_BELOW',\
 'STYLE_CLASS_SCROLLBAR', 'STYLE_CLASS_SCROLLBARS_JUNCTION', 'STYLE_CLASS_SEPARATOR',\
 'STYLE_CLASS_SIDEBAR', 'STYLE_CLASS_SLIDER', 'STYLE_CLASS_SPINBUTTON', 'STYLE_CLASS_SPINNER',\
 'STYLE_CLASS_TITLEBAR', 'STYLE_CLASS_TOOLBAR', 'STYLE_CLASS_TOOLTIP', 'STYLE_CLASS_TOP',\
 'STYLE_CLASS_TROUGH', 'STYLE_CLASS_VERTICAL', 'STYLE_CLASS_VIEW', 'STYLE_CLASS_WARNING',\
 'STYLE_PROPERTY_BACKGROUND_COLOR', 'STYLE_PROPERTY_BACKGROUND_IMAGE',\
 'STYLE_PROPERTY_BORDER_COLOR', 'STYLE_PROPERTY_BORDER_RADIUS', 'STYLE_PROPERTY_BORDER_STYLE',\
 'STYLE_PROPERTY_BORDER_WIDTH', 'STYLE_PROPERTY_COLOR', 'STYLE_PROPERTY_FONT',\
 'STYLE_PROPERTY_MARGIN', 'STYLE_PROPERTY_PADDING', 'STYLE_PROVIDER_PRIORITY_APPLICATION',\
 'STYLE_PROVIDER_PRIORITY_FALLBACK', 'STYLE_PROVIDER_PRIORITY_SETTINGS',\
 'STYLE_PROVIDER_PRIORITY_THEME', 'STYLE_PROVIDER_PRIORITY_USER', 'STYLE_REGION_COLUMN',\
 'STYLE_REGION_COLUMN_HEADER', 'STYLE_REGION_ROW', 'STYLE_REGION_TAB', 'Scale', 'ScaleButton',\
 'ScaleButtonClass', 'ScaleButtonPrivate', 'ScaleClass', 'ScalePrivate', 'ScrollStep',\
 'ScrollType', 'Scrollable', 'ScrollableInterface', 'ScrollablePolicy', 'Scrollbar',\
 'ScrollbarClass', 'ScrolledWindow', 'ScrolledWindowClass', 'ScrolledWindowPrivate',\
 'SearchBar', 'SearchBarClass', 'SearchEntry', 'SearchEntryClass', 'SelectionData',\
 'SelectionMode', 'SensitivityType', 'Separator', 'SeparatorClass', 'SeparatorMenuItem',\
 'SeparatorMenuItemClass', 'SeparatorPrivate', 'SeparatorToolItem', 'SeparatorToolItemClass',\
 'SeparatorToolItemPrivate', 'Settings', 'SettingsClass', 'SettingsPrivate', 'SettingsValue',\
 'ShadowType', 'SizeGroup', 'SizeGroupClass', 'SizeGroupMode', 'SizeGroupPrivate',\
 'SizeRequestMode', 'Socket', 'SocketClass', 'SocketPrivate', 'SortType', 'SpinButton',\
 'SpinButtonClass', 'SpinButtonPrivate', 'SpinButtonUpdatePolicy', 'SpinType', 'Spinner',\
 'SpinnerClass', 'SpinnerPrivate', 'Stack', 'StackClass', 'StackSwitcher', 'StackSwitcherClass',\
 'StackTransitionType', 'StateFlags', 'StateType', 'StatusIcon', 'StatusIconClass',\
 'StatusIconPrivate', 'Statusbar', 'StatusbarClass', 'StatusbarPrivate', 'StockItem', 'Style',\
 'StyleClass', 'StyleContext', 'StyleContextClass', 'StyleContextPrivate', 'StyleProperties',\
 'StylePropertiesClass', 'StylePropertiesPrivate', 'StyleProvider', 'StyleProviderIface',\
 'Switch', 'SwitchClass', 'SwitchPrivate', 'SymbolicColor', 'TEXT_VIEW_PRIORITY_VALIDATE',\
 'Table', 'TableChild', 'TableClass', 'TablePrivate', 'TableRowCol', 'TargetEntry',\
 'TargetFlags', 'TargetList', 'TearoffMenuItem', 'TearoffMenuItemClass', \
 'TearoffMenuItemPrivate', 'TextAppearance', 'TextAttributes', 'TextBTree', 'TextBuffer',\
 'TextBufferClass', 'TextBufferPrivate', 'TextBufferTargetInfo', 'TextChildAnchor', \
 'TextChildAnchorClass', 'TextDirection', 'TextIter', 'TextMark', 'TextMarkClass',\
 'TextSearchFlags', 'TextTag', 'TextTagClass', 'TextTagPrivate', 'TextTagTable',\
 'TextTagTableClass', 'TextTagTablePrivate', 'TextView', 'TextViewClass', 'TextViewPrivate',\
 'TextWindowType', 'ThemeEngine', 'ThemingEngine', 'ThemingEngineClass', 'ThemingEnginePrivate',\
 'ToggleAction', 'ToggleActionClass', 'ToggleActionEntry', 'ToggleActionPrivate', \
 'ToggleButton', 'ToggleButtonClass', 'ToggleButtonPrivate', 'ToggleToolButton', \
 'ToggleToolButtonClass', 'ToggleToolButtonPrivate', 'ToolButton', 'ToolButtonClass',\
 'ToolButtonPrivate', 'ToolItem', 'ToolItemClass', 'ToolItemGroup', 'ToolItemGroupClass', \
 'ToolItemGroupPrivate', 'ToolItemPrivate', 'ToolPalette', 'ToolPaletteClass',\
 'ToolPaletteDragTargets', 'ToolPalettePrivate', 'ToolShell', 'ToolShellIface', 'Toolbar',\
 'ToolbarClass', 'ToolbarPrivate', 'ToolbarSpaceStyle', 'ToolbarStyle', 'Tooltip',\
 'TreeDragDest', 'TreeDragDestIface', 'TreeDragSource', 'TreeDragSourceIface', 'TreeIter',\
 'TreeModel', 'TreeModelFilter', 'TreeModelFilterClass', 'TreeModelFilterPrivate',\
 'TreeModelFlags', 'TreeModelIface', 'TreeModelRow', 'TreeModelRowIter', 'TreeModelSort',\
 'TreeModelSortClass', 'TreeModelSortPrivate', 'TreePath', 'TreeRowReference', 'TreeSelection',\
 'TreeSelectionClass', 'TreeSelectionPrivate', 'TreeSortable', 'TreeSortableIface', 'TreeStore',\
 'TreeStoreClass', 'TreeStorePrivate', 'TreeView', 'TreeViewClass', 'TreeViewColumn',\
 'TreeViewColumnClass', 'TreeViewColumnPrivate', 'TreeViewColumnSizing', 'TreeViewDropPosition',\
 'TreeViewGridLines', 'TreeViewPrivate', 'UIManager', 'UIManagerClass', 'UIManagerItemType',\
 'UIManagerPrivate', 'Unit', 'VBox', 'VBoxClass', 'VButtonBox', 'VButtonBoxClass', 'VPaned',\
 'VPanedClass', 'VScale', 'VScaleClass', 'VScrollbar', 'VScrollbarClass', 'VSeparator', \
 'VSeparatorClass', 'Viewport', 'ViewportClass', 'ViewportPrivate', 'VolumeButton',\
 'VolumeButtonClass', 'Widget', 'WidgetAuxInfo', 'WidgetClass', 'WidgetClassPrivate', \
 'WidgetHelpType', 'WidgetPath', 'WidgetPrivate', 'Window', 'WindowClass', 'WindowGeometryInfo',\
 'WindowGroup', 'WindowGroupClass', 'WindowGroupPrivate', 'WindowPosition', 'WindowPrivate',\
 'WindowType', 'WrapMode', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__',\
 '__file__', '__format__', '__getattr__', '__getattribute__', '__hash__', '__init__', \
 '__loader__', '__module__', '__name__', '__new__', '__path__', '__reduce__', '__reduce_ex__',\
 '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',\
 '_construct_target_list', '_introspection_module', '_load', '_namespace', '_overrides_module',\
 '_version', 'accel_groups_activate', 'accel_groups_from_object',\
 'accelerator_get_default_mod_mask', 'accelerator_get_label',\
 'accelerator_get_label_with_keycode', 'accelerator_name', 'accelerator_name_with_keycode',\
 'accelerator_parse', 'accelerator_parse_with_keycode', 'accelerator_set_default_mod_mask',\
 'accelerator_valid', 'alternative_dialog_button_order', 'binding_entry_add_signal_from_string',\
 'binding_entry_add_signall', 'binding_entry_remove', 'binding_entry_skip', 'binding_set_find',\
 'bindings_activate', 'bindings_activate_event', 'builder_error_quark',\
 'cairo_should_draw_window', 'cairo_transform_to_window', 'check_version',\
 'css_provider_error_quark', 'device_grab_add', 'device_grab_remove', 'disable_setlocale',\
 'distribute_natural_allocation', 'drag_finish', 'drag_get_source_widget', \
 'drag_set_icon_default', 'drag_set_icon_gicon', 'drag_set_icon_name', 'drag_set_icon_pixbuf',\
 'drag_set_icon_stock', 'drag_set_icon_surface', 'drag_set_icon_widget',\
 'draw_insertion_cursor', 'events_pending', 'false', 'file_chooser_error_quark',\
 'get_binary_age', 'get_current_event', 'get_current_event_device', 'get_current_event_state', \
 'get_current_event_time', 'get_debug_flags', 'get_default_language', 'get_event_widget',\
 'get_interface_age', 'get_major_version', 'get_micro_version', 'get_minor_version',\
 'grab_get_current', 'icon_size_from_name', 'icon_size_get_name', 'icon_size_lookup',\
 'icon_size_lookup_for_settings', 'icon_size_register', 'icon_size_register_alias',\
 'icon_theme_error_quark', 'init', 'init_check', 'init_with_args', 'key_snooper_remove',\
 'main', 'main_do_event', 'main_iteration', 'main_iteration_do', 'main_level', 'main_quit',\
 'paint_arrow', 'paint_box', 'paint_box_gap', 'paint_check', 'paint_diamond', 'paint_expander',\
 'paint_extension', 'paint_flat_box', 'paint_focus', 'paint_handle', 'paint_hline',\
 'paint_layout', 'paint_option', 'paint_resize_grip', 'paint_shadow', 'paint_shadow_gap',\
 'paint_slider', 'paint_spinner', 'paint_tab', 'paint_vline', 'paper_size_get_default',\
 'paper_size_get_paper_sizes', 'parse_args', 'print_error_quark', 'print_run_page_setup_dialog',\
 'print_run_page_setup_dialog_async', 'propagate_event', 'rc_add_default_file',\
 'rc_find_module_in_path', 'rc_find_pixmap_in_path', 'rc_get_default_files',\
 'rc_get_im_module_file', 'rc_get_im_module_path', 'rc_get_module_dir', 'rc_get_style',\
 'rc_get_style_by_paths', 'rc_get_theme_dir', 'rc_parse', 'rc_parse_color', \
 'rc_parse_color_full', 'rc_parse_priority', 'rc_parse_state', 'rc_parse_string',\
 'rc_property_parse_border', 'rc_property_parse_color', 'rc_property_parse_enum',\
 'rc_property_parse_flags', 'rc_property_parse_requisition', 'rc_reparse_all',\
 'rc_reparse_all_for_settings', 'rc_reset_styles', 'rc_set_default_files',\
 'recent_chooser_error_quark', 'recent_manager_error_quark', 'render_activity',\
 'render_arrow', 'render_background', 'render_check', 'render_expander', 'render_extension',\
 'render_focus', 'render_frame', 'render_frame_gap', 'render_handle', 'render_icon',\
 'render_icon_pixbuf', 'render_icon_surface', 'render_insertion_cursor', 'render_layout',\
 'render_line', 'render_option', 'render_slider', 'rgb_to_hsv', 'selection_add_target',\
 'selection_add_targets', 'selection_clear_targets', 'selection_convert', 'selection_owner_set',\
 'selection_owner_set_for_display', 'selection_remove_all', 'set_debug_flags', 'show_uri',\
 'stock_add', 'stock_add_static', 'stock_list_ids', 'stock_lookup', 'stock_set_translate_func',\
 'target_table_free', 'target_table_new_from_list', 'targets_include_image', \
 'targets_include_rich_text', 'targets_include_text', 'targets_include_uri', \
 'test_create_simple_window', 'test_find_label', 'test_find_sibling', 'test_find_widget',\
 'test_list_all_types', 'test_register_all_types', 'test_slider_get_value', \
 'test_slider_set_perc', 'test_spin_button_click', 'test_text_get', 'test_text_set',\
 'test_widget_click', 'test_widget_send_key', 'test_widget_wait_for_draw',\
 'tree_get_row_drag_data', 'tree_row_reference_deleted', 'tree_row_reference_inserted',\
 'tree_set_row_drag_data', 'true']
"""