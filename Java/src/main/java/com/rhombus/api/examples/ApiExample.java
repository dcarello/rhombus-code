package com.rhombus.api.examples;

import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.rhombus.ApiClient;
import com.rhombus.sdk.CameraWebserviceApi;
import com.rhombus.sdk.domain.*;
import org.apache.http.Header;
import org.apache.http.message.BasicHeader;
import org.glassfish.jersey.jackson.internal.jackson.jaxrs.json.JacksonJaxbJsonProvider;

import javax.net.ssl.HostnameVerifier;
import javax.net.ssl.SSLSession;
import javax.ws.rs.client.ClientBuilder;
import java.util.ArrayList;
import java.util.List;

public class ApiExample
{
    private static ApiClient _apiClient;
    // private static final Logger _logger = LoggerFactory.getLogger(CopyFootageToLocalStorage.class);

    public static void main(String[] args) throws Exception
    {

        final String apiKey = "9Ts3iQ_HSZGHEqwxZnPKpA";
        final List<Header> defaultHeaders = new ArrayList<>();
        defaultHeaders.add(new BasicHeader("x-auth-scheme", "api-token"));
        defaultHeaders.add(new BasicHeader("x-auth-apikey", apiKey));

        final ClientBuilder clientBuilder = ClientBuilder.newBuilder();
        clientBuilder.register(new JacksonJaxbJsonProvider().configure(SerializationFeature.FAIL_ON_EMPTY_BEANS, false).configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false));

//        if(keystoreFile != null)
//        {
//            final KeyStore keyStore = KeyStore.getInstance("PKCS12");
//
//            try (final FileInputStream fileInputStream = new FileInputStream(keystoreFile))
//            {
//                keyStore.load(fileInputStream, keystorePassword);
//            }
//
//            final SSLContext sslContext = SSLContexts.custom().loadTrustMaterial(new TrustStrategy()
//            {
//                @Override
//                public boolean isTrusted(X509Certificate[] chain, String authType) throws CertificateException
//                {
//                    return true;
//                }
//            }).loadKeyMaterial(keyStore, keystorePassword).setProtocol("TLSv1.2").build();
//
//            clientBuilder.sslContext(sslContext);
//        }

        final HostnameVerifier hostnameVerifier = new HostnameVerifier()
        {
            @Override
            public boolean verify(String hostname, SSLSession session)
            {
                return true;
            }
        };

        clientBuilder.hostnameVerifier(hostnameVerifier);

        _apiClient = new ApiClient();
        _apiClient.setHttpClient(clientBuilder.build());
        _apiClient.addDefaultHeader("x-auth-scheme", "api-token");
        _apiClient.addDefaultHeader("x-auth-apikey", apiKey);

        // API call to the Minimal Camera State List
        final CameraWebserviceApi cameraWebservice = new CameraWebserviceApi(_apiClient);
        final CameraGetMinimalCameraStateListWSRequest getMinimalCameraStateRequest = new CameraGetMinimalCameraStateListWSRequest();
        // use this to set the parameters :getMinimalCameraStateRequest.setIncludeMummified(parameter);
        final CameraGetMinimalCameraStateListWSResponse getMinimalCameraStateListResponse = cameraWebservice.getMinimalCameraStateList(getMinimalCameraStateRequest);

        System.out.println(getMinimalCameraStateListResponse);

        // Goes through the Java Object from the API and gets the name and prints it
        final List <MinimalDeviceStateType> list = getMinimalCameraStateListResponse.getCameraStates();
        for( MinimalDeviceStateType cam : list)
        {
            String name = cam.getName();
            System.out.println(name);
        }

        final CameraGetConfigWSRequest configRequest = new CameraGetConfigWSRequest();
        configRequest.setCameraUuid("SdFCcHcOTwa4HcSZ3CpsFQ");
        final CameraGetConfigWSResponse configResponse = cameraWebservice.getConfig(configRequest);
        System.out.println(configResponse);

//        final CameraGetMinimalCameraStateListWSRequest getRequest = new CameraGetMinimalCameraStateListWSRequest();
//        final CameraGetMinimalCameraStateListWSResponse response = cameraWebservice.getMinimalCameraStateList(getRequest);
//        List<MinimalDeviceStateType> list = response.getCameraStates();
//        for (MinimalDeviceStateType cam : list)
//        {
//            String name = cam.getName();
//            _logger.info("name: {}", name);
//        }



    }
}
