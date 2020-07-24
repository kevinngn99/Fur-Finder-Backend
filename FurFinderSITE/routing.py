from django.conf.urls import url
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostOriginValidator,OriginValidator
from chat.consumer import ChatConsumer

application = ProtocolTypeRouter({
    'websocket' : AllowedHostOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    url(r"^messages/(?P<username>[\w.@+-]+)$", ChatConsumer),
                ]
            )
        )
    )
})
