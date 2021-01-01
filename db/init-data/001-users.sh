#!/bin/bash
set -e;

# a default non-root role
MONGO_NON_ROOT_ROLE="${MONGO_NON_ROOT_ROLE:-readWrite}"

if [ -n "${MONGO_INITDB__USERNAME:-}" ] && [ -n "${MONGO_INITDB_ROOT_PASSWORD:-}" ]; then
    "${mongo[@]}" "$MONGO_INITDB_DATABASE" <<-EOJS
   		db.createUser({
    			user: $(_js_escape "$MONGO_INITDB_USERNAME"),
    			pwd: $(_js_escape "$MONGO_INITDB_PASSWORD"),
    			roles: [ { role: $(_js_escape "$MONGO_NON_ROOT_ROLE"), db: $(_js_escape "$MONGO_INITDB_DATABASE") } ]
    			})
    	EOJS
    else
    	# print warning or kill temporary mongo and exit non-zero
    fi

