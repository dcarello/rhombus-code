package com.rhombus.api.examples;

import ch.qos.logback.classic.Level;
import ch.qos.logback.classic.LoggerContext;
import com.rhombus.ApiClient;
import org.apache.commons.cli.*;
import org.apache.http.Header;
import org.apache.http.message.BasicHeader;
import org.slf4j.LoggerFactory;

import javax.ws.rs.client.ClientBuilder;
import java.io.FileOutputStream;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.List;
import java.util.concurrent.TimeUnit;


public class Add_Remove_Labels {

    public Add_Remove_Labels() {

    }

    private static ApiClient _apiClient;

    public static void main(String[] args) throws Exception
    {
        Add_Remove_Labels instance = new Add_Remove_Labels();


        final Options options = new Options();
        options.addRequiredOption("a", "apikey", true, "API Key");
        options.addRequiredOption("c", "choice", true, "Add or remove a label");
        options.addRequiredOption("l", "label", true, "Label name");
        options.addRequiredOption("n", "names", true, "Names of people to add or remove labels from (ex: name, name, name)");

        final CommandLine commandLine;
        try
        {
            commandLine = new DefaultParser().parse(options, args);
        }
        catch (ParseException e)
        {
            System.err.println(e.getMessage());

            new HelpFormatter().printHelp(
                    "java -cp build/libs/rhombus-api-examples-all.jar com.rhombus.api.examples.CopyFootageToLocalStorage",
                    options);
            return;
        }

        final String apiKey = commandLine.getOptionValue("apikey");


    }

    private void api_call(final String apiKey) throws Exception
    {
    }

    private void _initialize(final String apiKey) throws Exception
    {
        /*
         * API CLIENT
         */
        {
            final List<Header> defaultHeaders = new ArrayList<>();
            defaultHeaders.add(new BasicHeader("x-auth-scheme", "api-token"));
            defaultHeaders.add(new BasicHeader("x-auth-apikey", apiKey));

            final ClientBuilder clientBuilder = ClientBuilder.newBuilder();

            _apiClient = new ApiClient();
            _apiClient.setHttpClient(clientBuilder.build());
            _apiClient.addDefaultHeader("x-auth-scheme", "api-token");
            _apiClient.addDefaultHeader("x-auth-apikey", apiKey);
        }
    }

}
