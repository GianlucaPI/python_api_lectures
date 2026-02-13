<?php

/**
 * QUANDO HA SENSO CHE PHP FACCIA UNA POST A UN ALTRO SERVER?
 * ----------------------------------------------------------
 * Anche se PHP è spesso usato per generare HTML, è comunissimo usarlo come client HTTP "Backend-to-Backend".
 * Ecco alcuni casi d'uso reali:
 * 
 * 1. Microservizi: Un sito e-commerce in PHP (es. Magento/WooCommerce) invia i dati di un ordine 
 *    appena concluso a un server gestionale separato (es. Python/Java) per la logistica.
 * 2. Integrazione AI/ML: Il sito PHP raccoglie input utente e li invia via POST a un'API Python 
 *    (come questa in Flask) che fa girare un modello di Machine Learning e restituisce la previsione.
 * 3. Webhooks & Notifiche: Il server PHP notifica un servizio esterno (es. Slack, Discord, o un CRM) 
 *    che è avvenuto un evento (registrazione utente, pagamento fallito).
 * 4. Disaccoppiamento: Migrare pezzi di logica pesante fuori dal server web principale per scalarli separatamente.
 */

$url = "http://127.0.0.1:5002/api/processa";

// I dati che vogliamo inviare
$data = array(
    "nome" => "Luigi",
    "cognome" => "Verdi",
    "linguaggio" => "PHP"
);

// Codifichiamo i dati in JSON
$json_data = json_encode($data);

// Configuriamo le opzioni del contesto HTTP per la richiesta POST
$options = array(
    'http' => array(
        'header'  => "Content-type: application/json\r\n", // Importante!
        'method'  => 'POST',
        'content' => $json_data,
        // Opzionale: gestire errori 4xx/5xx senza sollevare warning
        'ignore_errors' => true 
    )
);

// Creiamo il contesto
$context  = stream_context_create($options);

echo "Inviando richiesta POST a $url...\n";
echo "Dati inviati:\n$json_data\n\n";

// Eseguiamo la richiesta
$response = file_get_contents($url, false, $context);

if ($response === FALSE) {
    echo "Errore durante la richiesta.\n";
} else {
    // Decodifica la risposta
    $result_data = json_decode($response, true);
    
    echo "--- Risposta dal Server ---\n";
    if (json_last_error() === JSON_ERROR_NONE) {
        print_r($result_data);
    } else {
        echo $response;
    }
}

?>
