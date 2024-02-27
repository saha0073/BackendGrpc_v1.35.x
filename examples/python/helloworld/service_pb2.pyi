from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AudioConfig(_message.Message):
    __slots__ = ("sample_rate_hertz", "disable_audio", "enable_facial_data")
    SAMPLE_RATE_HERTZ_FIELD_NUMBER: _ClassVar[int]
    DISABLE_AUDIO_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FACIAL_DATA_FIELD_NUMBER: _ClassVar[int]
    sample_rate_hertz: int
    disable_audio: bool
    enable_facial_data: bool
    def __init__(self, sample_rate_hertz: _Optional[int] = ..., disable_audio: bool = ..., enable_facial_data: bool = ...) -> None: ...

class TriggerConfig(_message.Message):
    __slots__ = ("trigger_message",)
    TRIGGER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    trigger_message: str
    def __init__(self, trigger_message: _Optional[str] = ...) -> None: ...

class ActionConfig(_message.Message):
    __slots__ = ("actions", "characters", "objects", "classification", "context_level", "current_attention_object")
    class Character(_message.Message):
        __slots__ = ("name", "bio")
        NAME_FIELD_NUMBER: _ClassVar[int]
        BIO_FIELD_NUMBER: _ClassVar[int]
        name: str
        bio: str
        def __init__(self, name: _Optional[str] = ..., bio: _Optional[str] = ...) -> None: ...
    class Object(_message.Message):
        __slots__ = ("name", "description")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        name: str
        description: str
        def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ATTENTION_OBJECT_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedScalarFieldContainer[str]
    characters: _containers.RepeatedCompositeFieldContainer[ActionConfig.Character]
    objects: _containers.RepeatedCompositeFieldContainer[ActionConfig.Object]
    classification: str
    context_level: int
    current_attention_object: str
    def __init__(self, actions: _Optional[_Iterable[str]] = ..., characters: _Optional[_Iterable[_Union[ActionConfig.Character, _Mapping]]] = ..., objects: _Optional[_Iterable[_Union[ActionConfig.Object, _Mapping]]] = ..., classification: _Optional[str] = ..., context_level: _Optional[int] = ..., current_attention_object: _Optional[str] = ...) -> None: ...

class STTRequest(_message.Message):
    __slots__ = ("audio_config", "audio_chunk")
    AUDIO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CHUNK_FIELD_NUMBER: _ClassVar[int]
    audio_config: AudioConfig
    audio_chunk: bytes
    def __init__(self, audio_config: _Optional[_Union[AudioConfig, _Mapping]] = ..., audio_chunk: _Optional[bytes] = ...) -> None: ...

class STTResponse(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class GetResponseRequest(_message.Message):
    __slots__ = ("get_response_config", "get_response_data")
    class GetResponseConfig(_message.Message):
        __slots__ = ("character_id", "api_key", "session_id", "audio_config", "action_config", "speaker", "language_code")
        CHARACTER_ID_FIELD_NUMBER: _ClassVar[int]
        API_KEY_FIELD_NUMBER: _ClassVar[int]
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        AUDIO_CONFIG_FIELD_NUMBER: _ClassVar[int]
        ACTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
        SPEAKER_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
        character_id: str
        api_key: str
        session_id: str
        audio_config: AudioConfig
        action_config: ActionConfig
        speaker: str
        language_code: str
        def __init__(self, character_id: _Optional[str] = ..., api_key: _Optional[str] = ..., session_id: _Optional[str] = ..., audio_config: _Optional[_Union[AudioConfig, _Mapping]] = ..., action_config: _Optional[_Union[ActionConfig, _Mapping]] = ..., speaker: _Optional[str] = ..., language_code: _Optional[str] = ...) -> None: ...
    class GetResponseData(_message.Message):
        __slots__ = ("audio_data", "text_data", "trigger_data")
        AUDIO_DATA_FIELD_NUMBER: _ClassVar[int]
        TEXT_DATA_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_DATA_FIELD_NUMBER: _ClassVar[int]
        audio_data: bytes
        text_data: str
        trigger_data: TriggerConfig
        def __init__(self, audio_data: _Optional[bytes] = ..., text_data: _Optional[str] = ..., trigger_data: _Optional[_Union[TriggerConfig, _Mapping]] = ...) -> None: ...
    GET_RESPONSE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GET_RESPONSE_DATA_FIELD_NUMBER: _ClassVar[int]
    get_response_config: GetResponseRequest.GetResponseConfig
    get_response_data: GetResponseRequest.GetResponseData
    def __init__(self, get_response_config: _Optional[_Union[GetResponseRequest.GetResponseConfig, _Mapping]] = ..., get_response_data: _Optional[_Union[GetResponseRequest.GetResponseData, _Mapping]] = ...) -> None: ...

class GetResponseResponse(_message.Message):
    __slots__ = ("session_id", "action_response", "audio_response", "debug_log", "user_query", "bt_response")
    class AudioResponse(_message.Message):
        __slots__ = ("audio_data", "audio_config", "text_data", "end_of_response", "face_data")
        AUDIO_DATA_FIELD_NUMBER: _ClassVar[int]
        AUDIO_CONFIG_FIELD_NUMBER: _ClassVar[int]
        TEXT_DATA_FIELD_NUMBER: _ClassVar[int]
        END_OF_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        FACE_DATA_FIELD_NUMBER: _ClassVar[int]
        audio_data: bytes
        audio_config: AudioConfig
        text_data: str
        end_of_response: bool
        face_data: str
        def __init__(self, audio_data: _Optional[bytes] = ..., audio_config: _Optional[_Union[AudioConfig, _Mapping]] = ..., text_data: _Optional[str] = ..., end_of_response: bool = ..., face_data: _Optional[str] = ...) -> None: ...
    class ActionResponse(_message.Message):
        __slots__ = ("action",)
        ACTION_FIELD_NUMBER: _ClassVar[int]
        action: str
        def __init__(self, action: _Optional[str] = ...) -> None: ...
    class BehaviorTreeResponse(_message.Message):
        __slots__ = ("bt_code", "bt_constants", "narrative_section_id")
        BT_CODE_FIELD_NUMBER: _ClassVar[int]
        BT_CONSTANTS_FIELD_NUMBER: _ClassVar[int]
        NARRATIVE_SECTION_ID_FIELD_NUMBER: _ClassVar[int]
        bt_code: str
        bt_constants: str
        narrative_section_id: str
        def __init__(self, bt_code: _Optional[str] = ..., bt_constants: _Optional[str] = ..., narrative_section_id: _Optional[str] = ...) -> None: ...
    class UserTranscript(_message.Message):
        __slots__ = ("text_data", "is_final", "end_of_response")
        TEXT_DATA_FIELD_NUMBER: _ClassVar[int]
        IS_FINAL_FIELD_NUMBER: _ClassVar[int]
        END_OF_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        text_data: str
        is_final: bool
        end_of_response: bool
        def __init__(self, text_data: _Optional[str] = ..., is_final: bool = ..., end_of_response: bool = ...) -> None: ...
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DEBUG_LOG_FIELD_NUMBER: _ClassVar[int]
    USER_QUERY_FIELD_NUMBER: _ClassVar[int]
    BT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    action_response: GetResponseResponse.ActionResponse
    audio_response: GetResponseResponse.AudioResponse
    debug_log: str
    user_query: GetResponseResponse.UserTranscript
    bt_response: GetResponseResponse.BehaviorTreeResponse
    def __init__(self, session_id: _Optional[str] = ..., action_response: _Optional[_Union[GetResponseResponse.ActionResponse, _Mapping]] = ..., audio_response: _Optional[_Union[GetResponseResponse.AudioResponse, _Mapping]] = ..., debug_log: _Optional[str] = ..., user_query: _Optional[_Union[GetResponseResponse.UserTranscript, _Mapping]] = ..., bt_response: _Optional[_Union[GetResponseResponse.BehaviorTreeResponse, _Mapping]] = ...) -> None: ...

class GetResponseRequestSingle(_message.Message):
    __slots__ = ("response_config", "response_data")
    RESPONSE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_DATA_FIELD_NUMBER: _ClassVar[int]
    response_config: GetResponseRequest
    response_data: GetResponseRequest
    def __init__(self, response_config: _Optional[_Union[GetResponseRequest, _Mapping]] = ..., response_data: _Optional[_Union[GetResponseRequest, _Mapping]] = ...) -> None: ...

class HelloRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class HelloResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
