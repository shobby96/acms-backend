post_request_arg_types = {'userID': int,
                          'invitationTo': str,
                          'reason': str,
                          'status': int,
                          'date': str,
                          'timeOfArrival': str,
                          'persons': int,
                          'organizationID': int}

accept_request_arg_types = {'requestNumber': int}

cancel_request_arg_types = {'requestNumber': int,
                            'cancellationReason': str}


post_organization_arg_types = {
        'organization_name': str,
        'email': str,
}
