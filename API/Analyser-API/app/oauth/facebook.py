import json
from app.oauth.signin import OAuthSignIn
from rauth import OAuth1Service, OAuth2Service
from flask import current_app, url_for, request, redirect, session

class FacebookSignIn(OAuthSignIn):
    def __init__(self):
        super(FacebookSignIn, self).__init__('facebook')
        self.service = OAuth2Service(
            name='facebook',
            client_id=self.consumer_id,
            client_secret=self.consumer_secret,
            authorize_url='https://graph.facebook.com/v3.3/oauth/authorize',
            access_token_url='https://graph.facebook.com/v3.3/oauth/access_token',
            base_url='https://graph.facebook.com/v3.3/'
        )

    def authorize(self):
        return redirect(self.service.get_authorize_url(
            scope='email',
            response_type='code',
            redirect_uri=self.get_callback_url())
        )

    def callback(self):
        def decode_json(payload):
            return json.loads(payload.decode('utf-8'))

        if 'code' not in request.args:
            return None, None, None
        oauth_session = self.service.get_auth_session(
            data={'code': request.args['code'],
                  'grant_type': 'authorization_code',
                  'redirect_uri': self.get_callback_url()},
            decoder=decode_json
        )
        me = oauth_session.get('me?fields=id,email,name,short_name').json()
        return (
            'facebook$' + me['id'],
            me.get('email'),
            me.get('name'),
            me.get('short_name')
        )