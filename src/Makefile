# MAKEFILE

# Compiler
CC = gcc 

# Compiler Flags
CFLAGS = -g -Wall -Wextra

# Additional libraries
LDLIBS = -lraylib -lm -lpthread -ldl -lrt

# Executable name
TARGET = main 

# Source files
SOURCES = main.c 

# Object files
OBJECTS = $(SOURCES:.c=.o)

# Compile the source files into object files
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Link the object files into the executable
$(TARGET): $(OBJECTS)
	$(CC) $(CFLAGS) $^ -o $@ $(LDLIBS)

# Run the executable
run: $(TARGET)
	./$(TARGET)

# Clean up the generated files
clean:
	rm -rf $(OBJECTS) $(TARGET)
