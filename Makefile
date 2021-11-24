FLAGS="autostart"
TRUESHELL="$(echo $SHELL | sed 's/.*\/bin\///g')"

all: install run

run:
	@echo "Running termDash"
	@termDash

install:
	@echo "Installing termDash"
	@sudo ./scripts/install

	# Adds autostart capabilities if decided
	@if [[ "$(FLAGS)" == *"autostart"* ]]; then \
		echo "termDash" >> "/home/$(USER)/.$(TRUESHELL)rc"; \
	fi 

remove:
	@echo "Removing termDash"
	@sudo ./scripts/remove
