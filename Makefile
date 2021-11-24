FLAGS="autostart"

all: install run

run:
	@echo "Running termDash"
	@termDash

install:
	@echo "Installing termDash"
	@sudo ./scripts/install

	# Adds autostart capabilities if decided
	@if [[ "$(FLAGS)" == *"autostart"* ]]; then \
		echo "termDash" >> '/home/$(USER)/.$(shell echo $SHELL | sed 's/.*\/bin\///g')rc'; \
	fi 

remove:
	@echo "Removing termDash"
	@sudo ./scripts/remove
