from concurrent import futures
import grpc
from grpc_reflection.v1alpha import reflection as grpc_reflection
import random
import time
import service_pb2
import service_pb2_grpc
import os

# Enable debugging
os.environ["GRPC_TRACE"] = "all"
os.environ["GRPC_VERBOSITY"] = "WARNING"

class ConvaiService(service_pb2_grpc.ConvaiServiceServicer):

    def Hello(self, request, context):
        print("Hello function called with name:", request.name)
        return service_pb2.HelloResponse(message=f"Hello, {request.name}!")

    def HelloStream(self, request_iterator, context):
        print("HelloStream function called")
        for request in request_iterator:
            print("Streaming request received with name:", request.name)
            yield service_pb2.HelloResponse(message=f"Streaming Hello to {request.name}")

    def SpeechToText(self, request_iterator, context):
        print("SpeechToText function called")
        for request in request_iterator:
            print("SpeechToText request received with audio chunk:", request.audio_chunk[:10])
            response_text = f"Processed STT {request.audio_chunk[:10]}..."
            print("Sending response back to client:", response_text)
            yield service_pb2.STTResponse(text=response_text)

    def GetResponse(self, request_iterator, context):
        print("GetResponse function called")
        try:
            for request in request_iterator:
                print("GetResponse request received")
                # Create a dummy AudioConfig message
                audio_config = service_pb2.AudioConfig(
                    sample_rate_hertz=44100,
                    disable_audio=False,
                    enable_facial_data=True
                )
                # Create an AudioResponse message
                audio_response = service_pb2.GetResponseResponse.AudioResponse(
                    audio_data=b"From server dummy audio data",
                    audio_config=audio_config,
                    text_data="From server Dummy text data",
                    end_of_response=True,
                    face_data="From server Dummy face data"
                )
                # Generate response with AudioResponse
                yield service_pb2.GetResponseResponse(
                    session_id="dummy_session",
                    audio_response=audio_response  # Set the oneof field correctly
                )
        except Exception as e:
            print("Exception in GetResponse:", e)
            import traceback
            traceback.print_exc()  # Print the full stack trace

            context.set_code(grpc.StatusCode.INTERNAL)
            detailed_error_message = f"Error occurred: {e}\n{traceback.format_exc()}"
            context.set_details(detailed_error_message)
            return
    '''
    def GetResponse(self, request_iterator, context):
        print("GetResponse function called")
        try:
            for request in request_iterator:
                print("GetResponse request received")
                # Create a UserTranscript message
                user_transcript = service_pb2.GetResponseResponse_UserTranscript(
                    text_data="Dummy transcript text",
                    is_final=True,
                    end_of_response=True
                )
                # Generate response with UserTranscript
                yield service_pb2.GetResponseResponse(
                    session_id="dummy_session",
                    user_query=user_transcript  # Set the oneof field correctly
                )
        except Exception as e:
            print("Exception in GetResponse:", e)
            import traceback
            traceback.print_exc()  # Print the full stack trace

            context.set_code(grpc.StatusCode.INTERNAL)
            detailed_error_message = f"Error occurred: {e}\n{traceback.format_exc()}"
            context.set_details(detailed_error_message)
            return
    '''
    def GetResponseSingle(self, request, context):
        print("GetResponseSingle function called with request:", request)
        for i in range(5):
            print(f"Sending GetResponseSingle response {i + 1}")
            yield service_pb2.GetResponseResponse(
                session_id="dummy_session",
                response_type=service_pb2.GetResponseResponse.AudioResponse(
                    audio_data=b"dummy audio",
                    text_data="Dummy text"
                )
            )
            time.sleep(1)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_ConvaiServiceServicer_to_server(ConvaiService(), server)

    # Register the reflection service
    service_names = (
        service_pb2.DESCRIPTOR.services_by_name['ConvaiService'].full_name,
        grpc_reflection.SERVICE_NAME,
    )
    grpc_reflection.enable_server_reflection(service_names, server)

    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()