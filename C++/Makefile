CC = gcc
CXX = g++
AS = as

TARGET_APP = leetcode
BUILD_DIR ?= ./build
INC_DIRS ?= ./include
C_SRC_DIRS ?= ./

SRCS := $(shell find $(C_SRC_DIRS) -name "*.c" -or -name "*.cpp")
OBJS := $(SRCS:%=$(BUILD_DIR)/%.o)
DEPS := $(OBJS:.o=.d)

INC_FLAGS := $(addprefix -I,$(INC_DIRS))
LDPATHS := -L./
#LDFLAGS := -Wl,-Bdynamic -lfcsam -Wl,-Bstatic -lc++ -lc
#LDFLAGS := -Wl,-Bstatic -lfcsam -lc++ -lc

LOCAL_CFLAGS :=
LOCAL_CPPFLAGS :=

CFLAGS += $(INC_FLAGS) $(LOCAL_CFLAGS)
CPPFLAGS += $(INC_FLAGS) $(LOCAL_CPPFLAGS)

$(TARGET_APP): $(OBJS) 
	$(CXX) $(OBJS) -o $@ $(LDPATHS) $(LDFLAGS)

# c source
$(BUILD_DIR)/%.c.o: %.c
	$(MKDIR_P) $(dir $@)
	$(CC) $(CFLAGS) -c $< -o $@

# c++ source
$(BUILD_DIR)/%.cpp.o: %.cpp
	$(MKDIR_P) $(dir $@)
	$(CXX) $(CPPFLAGS) -c $< -o $@
all : $(TARGET_APP)

.PHONY: clean

clean:
	$(RM) -r $(BUILD_DIR) $(TARGET_APP)
-include $(DEPS)

MKDIR_P ?= mkdir -p
