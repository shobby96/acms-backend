post_request_arg_types = {'user_id': int,
                          'invitation_to': str,
                          'reason': str,
                          'status': int,
                          'invitation_date': str,
                          'invite_time': str,
                          'persons': int,
                          }

accept_request_arg_types = {'requestNumber': int}

cancel_request_arg_types = {'requestNumber': int,
                            'cancellationReason': str}


post_organization_arg_types = {
        'organization_name': str,
        'email': str,
        'user_id': int,
}

post_user_arg_types={
    'is_admin': bool,
    'first_name': str,
    'last_name': str
}


request_arg_types = {
    "request_number": int,
    "user_id": int,
    "invitation_to": str,
    "reason": str,
    "status": int,
    "invitation_date": str,
    "invite_time": str,
    "persons": int,
    "cancellation_reason": str,
    "organization_id": int
}

organization_arg_types = {
    "organization_id": int,
    "organization_name": str,
    "email": str
}

users_arg_types = {
    "user_id": int,
    "organization_id": int,
    "organization_name":str,
    "organization_email":str,
    "is_admin": bool,
    "first_name": str,
    "last_name": str,
    "email": str,
    "profile_image": str
}