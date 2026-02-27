<?php

// Configurazione URL Base (deve corrispondere alla porta di app.py)
$base_url = "http://127.0.0.1:5001";

/**
 * Funzione per eseguire una richiesta GET
 * 
 * PERCHÉ HA SENSO USARE PHP?
 * --------------------------
 * 1. Backend-to-Backend: Spesso le applicazioni PHP (come WordPress, Magento, Laravel) devono
 *    consumare microservizi esterni (come questa API Flask) per integrare dati.
 * 2. Disponibilità: PHP è presente sulla stragrande maggioranza dei server web condivisi.
 * 
 * PERCHÉ POTREBBE NON AVER SENSO?
 * -------------------------------
 * 1. Sincrono: Di default PHP è sincrono (blocca l'esecuzione finché l'API non risponde).
 *    In ambienti moderni (Node.js, Go), la gestione asincrona è più naturale.
 * 2. Configurazione: A seconda del server, `file_get_contents` potrebbe essere disabilitato
 *    per URL remoti (allow_url_fopen = Off), costringendo a usare cURL, che è più verboso.
 */
function fetch_endpoint($path) {
    global $base_url;
    $url = $base_url . $path;

    echo "\n--- Richiesta a: $url ---\n";

    // Utilizziamo file_get_contents per semplicità (richiede allow_url_fopen=On nel php.ini)
    // Per un uso più avanzato si dovrebbe usare cURL.
    // L'operatore @ sopprime i warning in caso di errore (gestito poi controllando $response)
    $response = @file_get_contents($url);

    if ($response === FALSE) {
        echo "Errore: Impossibile contattare l'endpoint.\n";
        echo "Suggerimento: Controlla che il server Flask sia attivo sulla porta 5001.\n";
    } else {
        // Tentiamo di decodificare se è JSON
        $json_data = json_decode($response, true);

        if (json_last_error() === JSON_ERROR_NONE) {
            echo "Risposta JSON decodificata:\n";
            print_r($json_data);
            
            // Esempio accesso dato specifico
            if (isset($json_data['messaggio'])) {
                echo "\nMessaggio specifico: " . $json_data['messaggio'] . "\n";
            }
        } else {
            echo "Risposta Testuale:\n";
            echo $response . "\n";
        }
    }
}

echo "Avvio Test Client PHP...\n";

// 1. Fetch Root (Testo semplice)
fetch_endpoint("/");

// 2. Fetch API JSON
fetch_endpoint("/api/saluto");

?>
