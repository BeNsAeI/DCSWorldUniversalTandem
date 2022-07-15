namespace DCSWorldUniversalTandem.SerialDeserial
{
    using System;
    using System.Collections.Generic;

    using System.Globalization;
    using Newtonsoft.Json;
    using Newtonsoft.Json.Converters;

    public partial class Plane
    {
        [JsonProperty("name")]
        public string Name { get; set; }

        [JsonProperty("crew")]
        public List<string> Crew { get; set; }

        [JsonProperty("roles")]
        public List<string> Roles { get; set; }

        [JsonProperty("cockpits")]
        public List<Cockpit> Cockpits { get; set; }

        [JsonProperty("seatAssignment")]
        public List<SeatAssignment> SeatAssignment { get; set; }

        [JsonProperty("actionBuffer")]
        public List<ActionBuffer> ActionBuffer { get; set; }
    }
}
