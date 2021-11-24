all: install run

run:
	@echo "Running termDash"
	@termDash

install:
	@echo "Installing termDash"
	@sudo ./scripts/install

remove:
	@echo "Removing termDash"
	@sudo ./scripts/remove
