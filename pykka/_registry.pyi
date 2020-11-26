import threading
from typing import Any, ClassVar, List, Optional, Type, Union, overload

from typing_extensions import Literal  # Py38+: Available in ``typing``

from pykka import Actor, ActorRef, Future

class ActorRegistry:
    _actor_refs: ClassVar[List[ActorRef]]
    _actor_refs_lock: ClassVar[threading.RLock]
    @classmethod
    def broadcast(
        cls, message: Any, target_class: Optional[Type[Actor]] = ...
    ) -> None: ...
    @classmethod
    def get_all(cls) -> List[ActorRef]: ...
    @classmethod
    def get_by_class(cls, actor_class: Type[Actor]) -> List[ActorRef]: ...
    @classmethod
    def get_by_class_name(cls, actor_class_name: str) -> List[ActorRef]: ...
    @classmethod
    def get_by_urn(cls, actor_urn: str) -> Optional[ActorRef]: ...
    @classmethod
    def register(cls, actor_ref: ActorRef) -> None: ...
    @overload
    @classmethod
    def stop_all(
        cls, block: Literal[True], timeout: Optional[float] = ...
    ) -> List[bool]: ...
    @overload  # noqa: Allow redefinition
    @classmethod
    def stop_all(
        cls, block: Literal[False], timeout: Optional[float] = ...
    ) -> List[Future[bool]]: ...
    @overload  # noqa: Allow redefinition
    @classmethod
    def stop_all(
        cls, block: bool = ..., timeout: Optional[float] = ...
    ) -> Union[
        List[bool], List[Future[bool]], List[Union[bool, Future[bool]]]
    ]: ...
    @classmethod
    def unregister(cls, actor_ref: ActorRef) -> None: ...