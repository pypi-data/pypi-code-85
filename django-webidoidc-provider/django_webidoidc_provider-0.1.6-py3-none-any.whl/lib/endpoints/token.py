import inspect
from base64 import urlsafe_b64encode
import hashlib
import logging
from django.contrib.auth import authenticate

from django.http import JsonResponse

from oidc_provider.lib.errors import (
    TokenError,
    UserAuthError,
)
from oidc_provider.lib.utils.oauth2 import extract_client_auth
from oidc_provider.lib.utils.token import (
    create_id_token,
    create_token,
    encode_id_token,
)
from oidc_provider.lib.utils.dpop import verify_dpop_proof
from oidc_provider.models import (
    Client,
    Code,
    Token,
    TokenType
)
from oidc_provider import settings

logger = logging.getLogger(__name__)


class TokenEndpoint(object):

    def __init__(self, request):
        self.request = request
        self.params = {}
        self.user = None
        self._extract_params()

    def _extract_params(self):
        client_id, client_secret = extract_client_auth(self.request)

        self.params['client_id'] = client_id
        self.params['client_secret'] = client_secret
        self.params['redirect_uri'] = self.request.POST.get('redirect_uri', '')
        self.params['grant_type'] = self.request.POST.get('grant_type', '')
        self.params['code'] = self.request.POST.get('code', '')
        self.params['state'] = self.request.POST.get('state', '')
        self.params['scope'] = self.request.POST.get('scope', '')
        self.params['refresh_token'] = self.request.POST.get('refresh_token', '')
        # PKCE parameter.
        self.params['code_verifier'] = self.request.POST.get('code_verifier')
        self.params['dpop'] = self.request.headers.get('dpop')

        self.params['username'] = self.request.POST.get('username', '')
        self.params['password'] = self.request.POST.get('password', '')

    def validate_params(self):
        try:
            self.client = Client.objects.get(client_id=self.params['client_id'])
        except Client.DoesNotExist:
            logger.debug('[Token] Client does not exist: %s', self.params['client_id'])
            raise TokenError('invalid_client')

        if self.client.client_type == 'confidential':
            if not (self.client.client_secret == self.params['client_secret']):
                logger.debug('[Token] Invalid client secret: client %s do not have secret %s',
                             self.client.client_id, self.client.client_secret)
                raise TokenError('invalid_client')

        if self.params['grant_type'] == 'authorization_code':
            if not (self.params['redirect_uri'] in self.client.redirect_uris):
                logger.debug('[Token] Invalid redirect uri: %s', self.params['redirect_uri'])
                raise TokenError('invalid_client')

            try:
                self.code = Code.objects.get(code=self.params['code'])
            except Code.DoesNotExist:
                logger.debug('[Token] Code does not exist: %s', self.params['code'])
                raise TokenError('invalid_grant')

            if not (self.code.client == self.client) \
               or self.code.has_expired():
                logger.debug('[Token] Invalid code: invalid client or code has expired')
                raise TokenError('invalid_grant')

            # Validate PKCE parameters.
            if self.params['code_verifier']:
                if self.code.code_challenge_method == 'S256':
                    new_code_challenge = urlsafe_b64encode(
                            hashlib.sha256(self.params['code_verifier'].encode('ascii')).digest()
                        ).decode('utf-8').replace('=', '')
                else:
                    new_code_challenge = self.params['code_verifier']

                if not (new_code_challenge == self.code.code_challenge):
                    raise TokenError('Unable to validate PKCE parameters! Code challenge failed')

            # Validate DPoP token.
            if self.params['dpop']:
                # validate signature
                verify_dpop_proof(self.request.headers.get('dpop'))

        elif self.params['grant_type'] == 'password':
            if not settings.get('OIDC_GRANT_TYPE_PASSWORD_ENABLE'):
                raise TokenError('unsupported_grant_type')

            auth_args = (self.request,)
            try:
                inspect.getcallargs(authenticate, *auth_args)
            except TypeError:
                auth_args = ()

            user = authenticate(
                *auth_args,
                username=self.params['username'],
                password=self.params['password']
            )

            if not user:
                raise UserAuthError()

            self.user = user

        elif self.params['grant_type'] == 'refresh_token':
            if not self.params['refresh_token']:
                logger.debug('[Token] Missing refresh token')
                raise TokenError('invalid_grant')

            try:
                self.token = Token.objects.get(refresh_token=self.params['refresh_token'],
                                               client=self.client)

            except Token.DoesNotExist:
                logger.debug(
                    '[Token] Refresh token does not exist: %s', self.params['refresh_token'])
                raise TokenError('invalid_grant')
        elif self.params['grant_type'] == 'client_credentials':
            if not self.client._scope:
                logger.debug('[Token] Client using client credentials with empty scope')
                raise TokenError('invalid_scope')
        else:
            logger.debug('[Token] Invalid grant type: %s', self.params['grant_type'])
            raise TokenError('unsupported_grant_type')

    def create_response_dic(self):
        if self.params['grant_type'] == 'authorization_code':
            return self.create_code_response_dic()
        elif self.params['grant_type'] == 'refresh_token':
            return self.create_refresh_response_dic()
        elif self.params['grant_type'] == 'password':
            return self.create_access_token_response_dic()
        elif self.params['grant_type'] == 'client_credentials':
            return self.create_client_credentials_response_dic()

    def _build_response_dictionary(self, token, id_token_dic=None, scope=None):
        return_dic = {
            'access_token': token.access_token,
            'refresh_token': token.refresh_token,
            'token_type': token.token_type,
            'expires_in': settings.get('OIDC_TOKEN_EXPIRE'),
        }

        if id_token_dic is not None:
            return_dic['id_token'] = encode_id_token(id_token_dic, token.client)

        if scope is not None:
            return_dic['scope'] = scope

        return return_dic

    def _get_token_type(self):
        if self.params['dpop']:
            return TokenType.DPoP
        return TokenType.Bearer

    def _get_default_aud(self):
        # TODO: https://git.startinblox.com/djangoldp-packages/django-webidoidc-provider/issues/10
        '''if self.params['dpop']:
            return self.client.website_url'''
        return self.client.client_id

    def create_code_response_dic(self):
        # See https://tools.ietf.org/html/rfc6749#section-4.1

        token = create_token(
            user=self.code.user,
            client=self.code.client,
            scope=self.code.scope,
            token_type=self._get_token_type(),
            request=self.request
        )

        if self.code.is_authentication:
            id_token_dic = create_id_token(
                user=self.code.user,
                aud=self._get_default_aud(),
                token=token,
                nonce=self.code.nonce,
                at_hash=token.at_hash,
                request=self.request,
                scope=token.scope,
            )
        else:
            id_token_dic = {}
        token.id_token = id_token_dic

        # Store the token.
        token.save()

        # We don't need to store the code anymore.
        self.code.delete()

        return self._build_response_dictionary(token, id_token_dic)

    def create_refresh_response_dic(self):
        # See https://tools.ietf.org/html/rfc6749#section-6

        scope_param = self.params['scope']
        scope = (scope_param.split(' ') if scope_param else self.token.scope)
        unauthorized_scopes = set(scope) - set(self.token.scope)
        if unauthorized_scopes:
            raise TokenError('invalid_scope')

        token = create_token(
            user=self.token.user,
            client=self.token.client,
            scope=scope,
            token_type=self._get_token_type(),
            request=self.request
        )

        # If the Token has an id_token it's an Authentication request.
        if self.token.id_token:
            id_token_dic = create_id_token(
                user=self.token.user,
                aud=self._get_default_aud(),
                token=token,
                nonce=None,
                at_hash=token.at_hash,
                request=self.request,
                scope=token.scope,
            )
        else:
            id_token_dic = {}
        token.id_token = id_token_dic

        # Store the token.
        token.save()

        # Forget the old token.
        self.token.delete()

        return self._build_response_dictionary(token, id_token_dic)

    def create_access_token_response_dic(self):
        # See https://tools.ietf.org/html/rfc6749#section-4.3

        token = create_token(
            self.user,
            self.client,
            self.params['scope'].split(' '),
            token_type=self._get_token_type(),
            request=self.request
        )

        id_token_dic = create_id_token(
            token=token,
            user=self.user,
            aud=self._get_default_aud(),
            nonce='self.code.nonce',
            at_hash=token.at_hash,
            request=self.request,
            scope=token.scope,
        )

        token.id_token = id_token_dic
        token.save()

        return self._build_response_dictionary(token, id_token_dic)

    def create_client_credentials_response_dic(self):
        # See https://tools.ietf.org/html/rfc6749#section-4.4.3

        token = create_token(
            user=None,
            client=self.client,
            scope=self.client.scope,
            token_type=self._get_token_type(),
            request=self.request
        )

        token.save()

        return_dic = self._build_response_dictionary(token, scope=self.client._scope)
        return_dic.pop('refresh_token')
        return return_dic

    @classmethod
    def response(cls, dic, status=200):
        """
        Create and return a response object.
        """
        response = JsonResponse(dic, status=status)
        response['Cache-Control'] = 'no-store'
        response['Pragma'] = 'no-cache'

        return response
