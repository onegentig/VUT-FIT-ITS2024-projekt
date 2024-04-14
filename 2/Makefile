ZIP_NAME=xonege00.zip

phony: zip test doc format ocstart ocstop oclogs ocrm

########## Zipping, docs etc. ##########

zip: $(ZIP_NAME)

doc: report.pdf

$(ZIP_NAME): report.pdf
	zip -9 -v $(ZIP_NAME) report.pdf requirements.txt environment.py features/*.feature features/steps/*.py

report.pdf: docs/report.typ
	typst compile docs/report.typ
	mv docs/report.pdf .

format:
	black environment.py features/steps/*.py

########## OpenCart & Selenium ##########

test: ocstart
	[ -f "requirements.txt" ] && pip3 install -r requirements.txt
	behave
	docker-compose down -v

ocstart: docker-compose.yml
	docker-compose up -d

ocstop:
	docker-compose down

oclogs:
	docker-compose logs -f

ocrm:
	docker-compose rm -f
