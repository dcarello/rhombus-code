package com.rhombus.api.examples;

import com.rhombus.ApiClient;
import com.rhombus.sdk.CameraWebserviceApi;
import com.rhombus.sdk.domain.CameraGetMediaUrisWSRequest;
import com.rhombus.sdk.domain.CameraGetMediaUrisWSResponse;
import com.rhombus.sdk.domain.CameraGetMinimalCameraStateListWSRequest;
import com.rhombus.sdk.domain.CameraGetMinimalCameraStateListWSResponse;
import org.apache.http.Header;
import org.apache.http.message.BasicHeader;
import org.apache.http.ssl.SSLContexts;
import org.apache.http.ssl.TrustStrategy;
import org.glassfish.jersey.jackson.JacksonFeature;
import sun.misc.Request;

import javax.net.ssl.HostnameVerifier;
import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLSession;
import javax.ws.rs.client.ClientBuilder;
import javax.xml.ws.Response;
import java.io.FileInputStream;
import java.security.KeyStore;
import java.security.cert.CertificateException;
import java.security.cert.X509Certificate;
import java.util.ArrayList;
import java.util.List;


public class ApiPractice
{
    private static ApiClient _apiClient;

    public static void main(String[] args) throws Exception
    {

        final String apiKey = "9Ts3iQ_HSZGHEqwxZnPKpA";
        final List<Header> defaultHeaders = new ArrayList<>();
        defaultHeaders.add(new BasicHeader("x-auth-scheme", "api-token"));
        defaultHeaders.add(new BasicHeader("x-auth-apikey", apiKey));

        final ClientBuilder clientBuilder = ClientBuilder.newBuilder();
        clientBuilder.register(JacksonFeature.class);

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


        final CameraWebserviceApi cameraWebservice = new CameraWebserviceApi(_apiClient);
        final CameraGetMinimalCameraStateListWSRequest getMinimalCameraStateRequest = new CameraGetMinimalCameraStateListWSRequest();
        final CameraGetMinimalCameraStateListWSResponse getMinimalCameraStateListResponse = cameraWebservice.getMinimalCameraStateList(getMinimalCameraStateRequest);
        System.out.println(getMinimalCameraStateListResponse);

    }
}
