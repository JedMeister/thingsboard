COMMON_OVERLAYS = confconsole-lapp nginx
COMMON_CONF = 

include $(FAB_PATH)/common/mk/turnkey/pgsql.mk
include $(FAB_PATH)/common/mk/turnkey.mk
