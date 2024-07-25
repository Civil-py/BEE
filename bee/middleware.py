
from django.utils.deprecation import MiddlewareMixin
import boto3
from jose import jwt
from django.conf import settings


class CognitoMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if not request.session.get('id_token'):
            return

        id_token = request.session.get('id_token')
        if id_token:
            try:
                response = requests.get(
                    f'https://cognito-idp.{settings.AWS_COGNITO_REGION}.amazonaws.com/{settings.AWS_COGNITO_USER_POOL_ID}/.well-known/jwks.json')
                keys = response.json().get('keys')
                kid = jwt.get_unverified_headers(id_token)['kid']
                key = next(k for k in keys if k['kid'] == kid)

                claims = jwt.decode(
                    id_token,
                    key,
                    algorithms=['RS256'],
                    audience=settings.AWS_COGNITO_APP_CLIENT_ID
                )
                request.user = claims  # Attach claims to request.user
            except Exception as e:
                print(f"Token validation error: {e}")
                request.user = None

