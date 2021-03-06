from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "frappe"
app_title = "Frappe Framework"
app_publisher = "Frappe Technologies"
app_description = "Full stack web framework with Python, Javascript, MariaDB, Redis, Node"
app_icon = "octicon octicon-circuit-board"
app_color = "orange"
source_link = "https://github.com/frappe/frappe"
app_license = "MIT"

app_email = "info@frappe.io"

before_install = "frappe.utils.install.before_install"
after_install = "frappe.utils.install.after_install"

page_js = {
	"setup-wizard": "public/js/frappe/setup_wizard.js"
}

# website
app_include_js = [
	"assets/js/libs.min.js",
	"assets/js/desk.min.js",
	"assets/js/editor.min.js",
	"assets/js/list.min.js",
	"assets/js/form.min.js",
	"assets/js/report.min.js",
	"assets/js/d3.min.js",
	"assets/frappe/js/frappe/toolbar.js"
]
app_include_css = [
	"assets/css/desk.min.css",
	"assets/css/list.min.css",
	"assets/css/form.min.css",
	"assets/css/report.min.css",
	"assets/css/module.min.css"
]

web_include_js = [
	"website_script.js"
]

bootstrap = "assets/frappe/css/bootstrap.css"
web_include_css = [
	"assets/css/frappe-web.css"
]
website_route_rules = [
	{"from_route": "/blog", "to_route": "Blog Post"},
	{"from_route": "/blog/<category>", "to_route": "Blog Post"}
]

write_file_keys = ["file_url", "file_name"]

notification_config = "frappe.core.notifications.get_notification_config"

before_tests = "frappe.utils.install.before_tests"

website_generators = ["Web Page", "Blog Post", "Blog Category", "Web Form"]

email_append_to = ["Event", "ToDo", "Communication"]

calendars = ["Event"]

# login

on_session_creation = [
	"frappe.core.doctype.communication.feed.login_feed",
	"frappe.core.doctype.user.user.notify_admin_access_to_system_manager",
	"frappe.limits.check_if_expired",
	"frappe.utils.scheduler.reset_enabled_scheduler_events",
]

# permissions

permission_query_conditions = {
	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
	"ToDo": "frappe.desk.doctype.todo.todo.get_permission_query_conditions",
	"User": "frappe.core.doctype.user.user.get_permission_query_conditions",
	"Note": "frappe.desk.doctype.note.note.get_permission_query_conditions",
}

has_permission = {
	"Event": "frappe.desk.doctype.event.event.has_permission",
	"ToDo": "frappe.desk.doctype.todo.todo.has_permission",
	"User": "frappe.core.doctype.user.user.has_permission",
	"Note": "frappe.desk.doctype.note.note.has_permission",
	"Communication": "frappe.core.doctype.communication.communication.has_permission"
}

standard_queries = {
	"User": "frappe.core.doctype.user.user.user_query"
}

doc_events = {
	"*": {
		"on_update": [
			"frappe.desk.notifications.clear_doctype_notifications",
			"frappe.core.doctype.communication.feed.update_feed"
		],
		"after_rename": "frappe.desk.notifications.clear_doctype_notifications",
		"on_cancel": [
			"frappe.desk.notifications.clear_doctype_notifications",
		],
		"on_trash": "frappe.desk.notifications.clear_doctype_notifications"
	},
	"Email Group Member": {
		"validate": "frappe.email.doctype.email_group.email_group.restrict_email_group"
	},

}

scheduler_events = {
	"all": [
		"frappe.email.queue.flush",
		"frappe.email.doctype.email_account.email_account.pull",
		"frappe.email.doctype.email_account.email_account.notify_unreplied",
	],
	"hourly": [
		"frappe.model.utils.link_count.update_link_count",
		'frappe.model.utils.list_settings.sync_list_settings',
		"frappe.utils.error.collect_error_snapshots"
	],
	"daily": [
		"frappe.email.queue.clear_outbox",
		"frappe.desk.notifications.clear_notifications",
		"frappe.core.doctype.error_log.error_log.set_old_logs_as_seen",
		"frappe.desk.doctype.event.event.send_event_digest",
		"frappe.sessions.clear_expired_sessions",
		"frappe.email.doctype.email_alert.email_alert.trigger_daily_alerts",
		"frappe.async.remove_old_task_logs",
		"frappe.utils.scheduler.disable_scheduler_on_expiry",
		"frappe.utils.scheduler.restrict_scheduler_events_if_dormant",
		"frappe.limits.update_space_usage",
		"frappe.email.doctype.auto_email_report.auto_email_report.send_daily",
		"frappe.desk.page.backups.backups.delete_downloadable_backups"
	],
	"daily_long": [
		"frappe.integrations.dropbox_integration.take_backups_daily"
	],
	"weekly_long": [
		"frappe.integrations.dropbox_integration.take_backups_weekly"
	],
	"monthly": [
		"frappe.email.doctype.auto_email_report.auto_email_report.send_monthly"
	]

}

get_translated_dict = {
	("doctype", "System Settings"): "frappe.geo.country_info.get_translated_dict",
	("page", "setup-wizard"): "frappe.geo.country_info.get_translated_dict"
}

sounds = [
	{"name": "email", "src": "/assets/frappe/sounds/email.mp3", "volume": 0.1},
	{"name": "submit", "src": "/assets/frappe/sounds/submit.mp3", "volume": 0.1},
	{"name": "cancel", "src": "/assets/frappe/sounds/cancel.mp3", "volume": 0.1},
	{"name": "delete", "src": "/assets/frappe/sounds/delete.mp3", "volume": 0.05},
	{"name": "click", "src": "/assets/frappe/sounds/click.mp3", "volume": 0.05},
	{"name": "error", "src": "/assets/frappe/sounds/error.mp3", "volume": 0.1},
	# {"name": "alert", "src": "/assets/frappe/sounds/alert.mp3"},
	# {"name": "chime", "src": "/assets/frappe/sounds/chime.mp3"},
]

bot_parsers = [
	'frappe.utils.bot.ShowNotificationBot',
	'frappe.utils.bot.GetOpenListBot',
	'frappe.utils.bot.ListBot',
	'frappe.utils.bot.FindBot',
	'frappe.utils.bot.CountBot'
]

setup_wizard_exception = "frappe.desk.page.setup_wizard.setup_wizard.email_setup_wizard_exception"
before_write_file = "frappe.limits.validate_space_limit"

integration_services = ["PayPal", "Razorpay", "Dropbox", "LDAP"]
